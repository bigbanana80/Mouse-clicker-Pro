import sys
import time
import os

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QPixmap

from mainUi import Ui_main_window

import threading
import keyboard
import pynput
import ctypes

from unittest.mock import patch

# ? replace this during build time with import pyautogui, its just there to get rid of the annoying error that the user will never see
with patch("ctypes.windll.user32.SetProcessDPIAware", autospec=True):
    import pyautogui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.timer = QtCore.QTimer()
        my_pixmap = QPixmap("icon.ico")
        self.my_icon = QIcon(my_pixmap)
        self.setWindowIcon(self.my_icon)

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

        self.__stop_threads = True  # ? start and stop btns depends on this

        # & startup tasks
        self.ui.le_hours.setText("0")
        self.ui.le_mins.setText("0")
        self.ui.le_s.setText("0")
        self.ui.le_ms.setText("100")

        self.ui.le_timer_h.setText("0")
        self.ui.le_timer_min.setText("0")
        self.ui.le_timer_s.setText("0")
        self.ui.le_timer_ms.setText("0")

        self.ui.le_hold_hours.setText("0")
        self.ui.le_hold_mins.setText("0")
        self.ui.le_hold_s.setText("0")
        self.ui.le_hold_ms.setText("0")

        self.ui.repeat_times.setValue(0)

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

        self.ui.le_hold_hours.textChanged.connect(self.update_vars)
        self.ui.le_hold_mins.textChanged.connect(self.update_vars)
        self.ui.le_hold_s.textChanged.connect(self.update_vars)
        self.ui.le_hold_ms.textChanged.connect(self.update_vars)

        self.ui.repeat_times.valueChanged.connect(self.update_vars)

        self.ui.repeat_opt_1.clicked.connect(self.repeat_opt)
        self.ui.repeat_opt_2.clicked.connect(self.repeat_opt)

        self.ui.pos_opt_1.clicked.connect(self.pos_opt)
        self.ui.pos_opt_2.clicked.connect(self.pos_opt)

        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_shortcut.clicked.connect(self.shortcut_change)
        self.ui.btn_help.clicked.connect(self.help_func)

        self.shortcut_start_stop = "F6"
        keyboard.add_hotkey(self.shortcut_start_stop, self.shortcut_func)

    def help_func(self):
        os.system('start "" https://github.com/bigbanana80/Mouse-clicker-Pro')

    def shortcut_change(self):
        keyboard.remove_hotkey(self.shortcut_start_stop)

        def on_press(key):
            # pynput.keyboard.Key.
            if isinstance(key, pynput.keyboard.KeyCode):
                self.shortcut_start_stop = key.char

            else:
                if key == pynput.keyboard.Key.f1:
                    self.shortcut_start_stop = "F1"

                elif key == pynput.keyboard.Key.f2:
                    self.shortcut_start_stop = "F2"

                elif key == pynput.keyboard.Key.f3:
                    self.shortcut_start_stop = "F3"

                elif key == pynput.keyboard.Key.f4:
                    self.shortcut_start_stop = "F4"

                elif key == pynput.keyboard.Key.f5:
                    self.shortcut_start_stop = "F5"

                elif key == pynput.keyboard.Key.f6:
                    self.shortcut_start_stop = "F6"

                elif key == pynput.keyboard.Key.f7:
                    self.shortcut_start_stop = "F7"

                elif key == pynput.keyboard.Key.f8:
                    self.shortcut_start_stop = "F8"

                elif key == pynput.keyboard.Key.f9:
                    self.shortcut_start_stop = "F9"

                elif key == pynput.keyboard.Key.f10:
                    self.shortcut_start_stop = "F10"

                elif key == pynput.keyboard.Key.f11:
                    self.shortcut_start_stop = "F11"

                elif key == pynput.keyboard.Key.f12:
                    self.shortcut_start_stop = "F12"

                elif key == pynput.keyboard.Key.home:
                    self.shortcut_start_stop = "home"

                elif key == pynput.keyboard.Key.insert:
                    self.shortcut_start_stop = "insert"

                elif key == pynput.keyboard.Key.delete:
                    self.shortcut_start_stop = "delete"

                elif key == pynput.keyboard.Key.end:
                    self.shortcut_start_stop = "end"

                elif key == pynput.keyboard.Key.page_up:
                    self.shortcut_start_stop = "page_up"

                elif key == pynput.keyboard.Key.page_down:
                    self.shortcut_start_stop = "page_down"

                elif key == pynput.keyboard.Key.pause:
                    self.shortcut_start_stop = "pause"

                elif key == pynput.keyboard.Key.backspace:
                    self.shortcut_start_stop = "backspace"

                elif key == pynput.keyboard.Key.enter:
                    self.shortcut_start_stop = "enter"

                elif key == pynput.keyboard.Key.space:
                    self.shortcut_start_stop = (
                        "F6"  # ? space does not work well for the time being
                    )

                else:
                    self.shortcut_start_stop = "F6"

        def on_release(key):
            keyboard.add_hotkey(self.shortcut_start_stop, self.shortcut_func)
            self.ui.btn_start.setText(f"Start({self.shortcut_start_stop})")
            self.ui.btn_stop.setText(f"Stop({self.shortcut_start_stop})")
            self.ui.btn_shortcut.setText(f"New Hotkey is ({self.shortcut_start_stop})")
            return False

        # Collect events until released
        with pynput.keyboard.Listener(
            on_press=on_press, on_release=on_release
        ) as listener:
            listener.join()

    def shortcut_func(self):
        if self.__stop_threads:
            self.start()
        else:
            self.stop()

    def click_inf(self, hold_time, delay, timer):
        if self.ui.comboB_mouse_btn.currentText() == "Left":
            down = self.MOUSEEVENTF_LEFTDOWN
            up = self.MOUSEEVENTF_LEFTUP
        elif self.ui.comboB_mouse_btn.currentText() == "Right":
            down = self.MOUSEEVENTF_RIGHTDOWN
            up = self.MOUSEEVENTF_RIGHTUP
        elif self.ui.comboB_mouse_btn.currentText() == "Middle":
            down = self.MOUSEEVENTF_MIDDLEDOWN
            up = self.MOUSEEVENTF_MIDDLEUP
        if self.ui.pos_opt_2.isChecked():
            x = int(self.ui.x_cor.text())
            y = int(self.ui.y_cor.text())
            pyautogui.moveTo(x, y)
        else:
            x = 0
            y = 0
        if timer == 0 and self.click_repeat == 0:
            while True:
                self.click(hold_time, up, down)
                time.sleep(delay)
                if self.__stop_threads == True:
                    return
        else:
            self.click_with_options(hold_time, delay, up, down)

    def click_with_options(self, hold_time, delay, up, down):
        if self.click_repeat > 0:
            temp = self.click_repeat
        else:
            temp = -1
        if self.click_timer > 0:
            self.thread_timer = threading.Thread(target=self.timer_countdown)
            self.thread_timer.start()
        while True:
            self.click(hold_time, up, down)
            temp -= 1
            time.sleep(delay)
            if self.__stop_threads == True or temp == 0:
                self.__stop_threads = True
                try:
                    if self.thread_timer.is_alive():
                        self.thread_timer.join(0.2)
                except AttributeError:
                    pass
                self.ui.btn_start.setDisabled(False)
                self.ui.btn_stop.setDisabled(True)
                return

    def click(self, hold_time, up, down):
        temp = self.click_type[self.ui.comboB_clickType.currentText()]
        for _ in range(temp):
            self.click_helper(hold_time, up, down)

    def click_helper(self, hold_time, up, down):
        ctypes.windll.user32.mouse_event(down, 0, 0, 0, 0)  # left down
        time.sleep(hold_time)
        ctypes.windll.user32.mouse_event(up, 0, 0, 0, 0)

    def timer_countdown(self):
        temp = self.click_timer
        time.sleep(temp)
        self.__stop_threads = True

    def start(self):
        self.ui.btn_shortcut.setEnabled(False)
        self.ui.btn_start.setDisabled(True)
        self.ui.btn_stop.setDisabled(False)
        self.click_thread = threading.Thread(
            target=self.click_inf,
            args=(self.click_hold, self.click_speed, self.click_timer),
        )
        self.__stop_threads = False
        self.click_thread.start()

    def stop(self):
        self.__stop_threads = True
        self.click_thread.join()
        self.ui.btn_start.setDisabled(False)
        self.ui.btn_stop.setDisabled(True)
        self.ui.btn_shortcut.setEnabled(True)

    def update_vars(self):
        try:
            self.click_speed = (
                int(self.ui.le_hours.text()) * 3600
                + int(self.ui.le_mins.text()) * 60
                + int(self.ui.le_s.text())
                + int(self.ui.le_ms.text()) / 1000
            )
        except ValueError:
            pass
        try:
            self.click_timer = (
                int(self.ui.le_timer_h.text()) * 3600
                + int(self.ui.le_timer_min.text()) * 60
                + int(self.ui.le_timer_s.text())
                + int(self.ui.le_timer_ms.text()) / 1000
            )
        except ValueError:
            pass
        try:
            self.click_hold = (
                int(self.ui.le_hold_hours.text()) * 3600
                + int(self.ui.le_hold_mins.text()) * 60
                + int(self.ui.le_hold_s.text())
                + int(self.ui.le_hold_ms.text()) / 1000
            )
        except ValueError:
            pass
        self.click_repeat = abs(int(self.ui.repeat_times.text()))
        self.click_type = {"Single": 1, "Double": 2, "Triple": 3}

    def repeat_opt(self):
        if self.ui.repeat_opt_1.isChecked():
            self.ui.repeat_times.setEnabled(True)
        else:
            self.ui.repeat_times.setEnabled(False)
            self.ui.repeat_times.setValue(0)

    def pos_opt(self):
        if self.ui.pos_opt_2.isChecked():
            self.ui.x_cor.setEnabled(True)
            self.ui.y_cor.setEnabled(True)
        else:
            self.ui.x_cor.setEnabled(False)
            self.ui.y_cor.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
