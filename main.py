import sys
import time
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Qt, QTranslator

from mainUi import Ui_main_window
import threading
import keyboard
import ctypes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()

        # & startup tasks
        self.ui.btn_stop.setDisabled(True)

        # & variables

        self.MOUSEEVENTF_MOVE = 0x0001  # mouse move
        self.MOUSEEVENTF_LEFTDOWN = 0x0002  # left button down
        self.MOUSEEVENTF_LEFTUP = 0x0004  # left button up
        self.MOUSEEVENTF_RIGHTDOWN = 0x0008  # right button down
        self.MOUSEEVENTF_RIGHTUP = 0x0010  # right button up
        self.MOUSEEVENTF_MIDDLEDOWN = 0x0020  # middle button down
        self.MOUSEEVENTF_MIDDLEUP = 0x0040  # middle button up
        self.MOUSEEVENTF_WHEEL = 0x0800  # wheel button rolled
        self.MOUSEEVENTF_ABSOLUTE = 0x8000  # absolute move

        self.ui.le_hours.setText("0")
        self.ui.le_mins.setText("0")
        self.ui.le_s.setText("0")
        self.ui.le_ms.setText("100")

        self.ui.le_timer_h.setText("0")
        self.ui.le_timer_min.setText("0")
        self.ui.le_timer_s.setText("0")
        self.ui.le_timer_ms.setText("0")

        """        
        self.ui.le_hours.setDisabled(True)
        self.ui.le_mins.setDisabled(True)
        self.ui.le_s.setDisabled(True)
        self.ui.le_ms.setDisabled(True)
        """  # ? might need to add lock and unlock functions

        self.__stop_threads = True  # ? start and stop btns depends on this

        self.update_vars()  # ? runs once to update properly

        # & Connections
        self.ui.le_hours.textChanged.connect(self.update_vars)
        self.ui.le_mins.textChanged.connect(self.update_vars)
        self.ui.le_s.textChanged.connect(self.update_vars)
        self.ui.le_ms.textChanged.connect(self.update_vars)

        self.ui.le_timer_h.textChanged.connect(self.update_vars)
        self.ui.le_timer_min.textChanged.connect(self.update_vars)
        self.ui.le_timer_s.textChanged.connect(self.update_vars)
        self.ui.le_timer_ms.textChanged.connect(self.update_vars)

        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)

        # ? Qshortcut is dogshit and doesnt work for my usecase
        """  
        shortcut = QtGui.QKeySequence(QTranslator.tr("Ctrl+B"))
        start_shortcut = QtGui.QShortcut(shortcut, self)
        start_shortcut.activated.connect(self.ui.btn_start.click)

        stop_shortcut = QtGui.QShortcut(shortcut, self)
        stop_shortcut.activated.connect(self.ui.btn_stop.click)
        self.shortcut_thread = threading.Thread(target=self.shortcut_func)
        self.shortcut_thread.start()
        
        """
        self.shortcut_start_stop = "F6"
        keyboard.add_hotkey(self.shortcut_start_stop, self.shortcut_func)

    def shortcut_func(self):
        if self.__stop_threads:
            self.start()
        else:
            self.stop()

    def click_inf(self, hold_time, mouse_btn, delay, timer):
        if self.ui.comboB_mouse_btn.currentText() == "Left":
            down = self.MOUSEEVENTF_LEFTDOWN
            up = self.MOUSEEVENTF_LEFTUP
        elif self.ui.comboB_mouse_btn.currentText() == "Right":
            down = self.MOUSEEVENTF_RIGHTDOWN
            up = self.MOUSEEVENTF_RIGHTUP
        elif self.ui.comboB_mouse_btn.currentText() == "Middle":
            down = self.MOUSEEVENTF_MIDDLEDOWN
            up = self.MOUSEEVENTF_MIDDLEUP

        if timer == 0:
            while True:
                ctypes.windll.user32.mouse_event(down, 0, 0, 0, 0)  # left down
                time.sleep(hold_time)
                ctypes.windll.user32.mouse_event(up, 0, 0, 0, 0)
                time.sleep(delay)
                if self.__stop_threads == True:
                    return
        else:
            self.click_with_time(hold_time, delay, timer, up, down)

    def click_with_time(self, hold_time, delay, timer, up, down):
        self.thread_timer = threading.Thread(target=self.timer_countdown)
        self.thread_timer.start()
        while True:
            ctypes.windll.user32.mouse_event(down, 0, 0, 0, 0)  # left down
            time.sleep(hold_time)
            ctypes.windll.user32.mouse_event(up, 0, 0, 0, 0)
            time.sleep(delay)
            if self.__stop_threads == True:
                self.ui.btn_start.setDisabled(False)
                self.ui.btn_stop.setDisabled(True)
                return

    def timer_countdown(self):
        temp = self.click_timer
        time.sleep(temp)
        self.__stop_threads = True

    def start(self):
        self.ui.btn_start.setDisabled(True)
        self.ui.btn_stop.setDisabled(False)
        self.click_thread = threading.Thread(
            target=self.click_inf, args=(0, "left", self.click_speed, self.click_timer)
        )
        self.__stop_threads = False
        self.click_thread.start()

    def stop(self):
        self.__stop_threads = True
        self.click_thread.join()
        self.ui.btn_start.setDisabled(False)
        self.ui.btn_stop.setDisabled(True)

    def update_vars(self):
        self.click_speed = (
            int(self.ui.le_hours.text()) * 3600
            + int(self.ui.le_mins.text()) * 60
            + int(self.ui.le_s.text())
            + int(self.ui.le_ms.text()) / 1000
        )
        self.click_timer = (
            int(self.ui.le_timer_h.text()) * 3600
            + int(self.ui.le_timer_min.text()) * 60
            + int(self.ui.le_timer_s.text())
            + int(self.ui.le_timer_ms.text()) / 1000
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
