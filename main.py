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
        self.ui.le_hours.setText("0")
        self.ui.le_mins.setText("0")
        self.ui.le_s.setText("0")
        self.ui.le_ms.setText("100")

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

    def click_inf(self, hold_time, mouse_btn, delay):
        while True:
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
            time.sleep(hold_time)
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
            time.sleep(delay)
            if self.__stop_threads == True:
                break

    def start(self):
        self.ui.btn_start.setDisabled(True)
        self.ui.btn_stop.setDisabled(False)
        self.click_thread = threading.Thread(
            target=self.click_inf, args=(0, "left", self.click_speed)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
