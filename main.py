import sys
import time
import os
import pathlib

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QSystemTrayIcon,
    QMenu,
)
from PySide6.QtGui import QIcon, QPixmap, QAction

from mainUi import Ui_main_window

from icecream import ic
from loguru import logger
import threading
import keyboard
import pynput
import ctypes

import configparser

SETTINGS = "settings.ini"


def validate_settings():
    # ? checks if setting.ini exist, if not make it with default settings
    if not os.path.exists(SETTINGS):
        with open(SETTINGS, "w") as file:
            config = configparser.ConfigParser()

            config["interval"] = {
                "hour": "0",
                "minute": "0",
                "second": "0",
                "milliseconds": "100",
            }
            config["holdTime"] = {
                "hour": "0",
                "minute": "0",
                "second": "0",
                "milliseconds": "0",
            }
            config["timer"] = {
                "hour": "0",
                "minute": "0",
                "second": "0",
                "milliseconds": "0",
            }
            config["settings"] = {"Mouse-btn": "Left", "Click-type": "Single"}
            config["repeat"] = {"repeat-times": "0", "repeat-type": "2"}
            config["position"] = {"pos-type": "1", "pos-x": "0", "pos-y": "0"}
            config["shortcuts"] = {"Activate-key": "F6", "Stop-key": "F6"}
            config["checkbox"] = {
                "tray_icon_visible": "False",
                "alt_click": "False",
            }
            config.write(file)


validate_settings()

# ? replace this during build time with import pyautogui, its just there to get rid of the annoying error that the user will never see
from unittest.mock import patch

with patch("ctypes.windll.user32.SetProcessDPIAware", autospec=True):
    import pyautogui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.config = configparser.ConfigParser()
        self.config.read("settings.ini")

        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.timer = QtCore.QTimer()
        self.icon_name = "icon.ico"
        my_pixmap = QPixmap(self.icon_name)
        self.my_icon = QIcon(my_pixmap)
        self.setWindowIcon(self.my_icon)
        logger.info("App successfully initiated.")
        # & variables

        self.MOUSE_EVENT_MOVE = 0x0001  # mouse move
        self.MOUSE_EVENT_LEFTDOWN = 0x0002  # left button down
        self.MOUSE_EVENT_LEFTUP = 0x0004  # left button up
        self.MOUSE_EVENT_RIGHTDOWN = 0x0008  # right button down
        self.MOUSE_EVENT_RIGHTUP = 0x0010  # right button up
        self.MOUSE_EVENT_MIDDLEDOWN = 0x0020  # middle button down
        self.MOUSE_EVENT_MIDDLEUP = 0x0040  # middle button up
        self.MOUSE_EVENT_WHEEL = 0x0800  # wheel button rolled
        self.MOUSE_EVENT_ABSOLUTE = 0x8000  # absolute move

        self.__stop_threads = (
            True  # ? start and stop buttons depends on this. True means it will stop
        )
        logger.info("thread successfully initiated.")

        # & startup tasks
        self.ui.le_hours.setText(self.config["interval"]["hour"])
        self.ui.le_mins.setText(self.config["interval"]["minute"])
        self.ui.le_s.setText(self.config["interval"]["second"])
        self.ui.le_ms.setText(self.config["interval"]["milliseconds"])

        self.ui.le_timer_h.setText(self.config["timer"]["hour"])
        self.ui.le_timer_min.setText(self.config["timer"]["minute"])
        self.ui.le_timer_s.setText(self.config["timer"]["second"])
        self.ui.le_timer_ms.setText(self.config["timer"]["milliseconds"])

        self.ui.le_hold_hours.setText(self.config["holdTime"]["hour"])
        self.ui.le_hold_mins.setText(self.config["holdTime"]["minute"])
        self.ui.le_hold_s.setText(self.config["holdTime"]["second"])
        self.ui.le_hold_ms.setText(self.config["holdTime"]["milliseconds"])

        self.ui.repeat_times.setValue(int(self.config["repeat"]["repeat-times"]))

        self.ui.tray_icon_visible.setChecked(
            bool(self.config.getboolean("checkbox", "tray_icon_visible"))
        )
        self.ui.alt_clk_checkbox.setChecked(
            bool(self.config.getboolean("checkbox", "alt_click"))
        )

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

        self.ui.alt_clk_checkbox.clicked.connect(self.alt_clk_checkbox_function)
        self.ui.tray_icon_visible.clicked.connect(self.tray_icon_visible_function)
        # & Tray icon and functionality
        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(QIcon(self.icon_name), self)

        # Create a context menu for the tray icon
        self.tray_menu = QMenu()
        self.restore_action = QAction("Open")
        self.restore_action.triggered.connect(self.restore_window)
        self.exit_action = QAction("Close")
        self.exit_action.triggered.connect(self.exit_app)

        self.tray_menu.addAction(self.restore_action)
        self.tray_menu.addAction(self.exit_action)

        self.tray_icon.setContextMenu(self.tray_menu)

        # Connect the activated signal to a method
        self.tray_icon.activated.connect(self.tray_icon_activated)

        if self.ui.tray_icon_visible.isChecked():
            self.tray_icon.show()

        # & Final tasks which has to do with shortcut btn
        self.shortcut_start_stop = self.config["shortcuts"]["activate-key"]
        keyboard.add_hotkey(self.shortcut_start_stop, self.shortcut_func)
        self.ui.btn_start.setText(f"Start({self.shortcut_start_stop})")
        self.ui.btn_stop.setText(f"Stop({self.shortcut_start_stop})")
        logger.info("initiation complete.")

    def help_func(self):
        os.system('start "" https://github.com/bigbanana80/Mouse-clicker-Pro')

    def shortcut_change(self):
        logger.info("changing shortcut")
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
            self.config["shortcuts"]["activate-key"] = self.shortcut_start_stop
            with open(SETTINGS, "w") as f:
                self.config.write(f)
            return False

        # Collect events until released
        with pynput.keyboard.Listener(
            on_press=on_press, on_release=on_release
        ) as listener:
            listener.join()
        logger.info("shortcut changed successfully")

    def shortcut_func(self):
        if self.__stop_threads:
            self.start()
        else:
            self.stop()

    def alt_click(self, hold_time, delay, timer):
        logger.info("Auto Clicker started.(alt)")
        if self.click_timer > 0:
            self.thread_timer = threading.Thread(target=self.timer_countdown)
            self.thread_timer.start()
        if self.ui.comboB_mouse_btn.currentText() == "Left":
            temp = "left"
        if self.ui.comboB_mouse_btn.currentText() == "Right":
            temp = "right"
        if self.ui.comboB_mouse_btn.currentText() == "Middle":
            temp = "middle"
        while True:
            pyautogui.mouseDown(button=temp)
            time.sleep(hold_time)
            pyautogui.mouseUp(button=temp)
            time.sleep(delay)
            if self.__stop_threads == True:
                try:
                    if self.thread_timer.is_alive():
                        self.thread_timer.join(0.2)
                except AttributeError:
                    pass
                self.ui.btn_start.setDisabled(False)
                self.ui.btn_stop.setDisabled(True)
                self.ui.btn_shortcut.setDisabled(False)
                logger.info("Auto Clicker ended")
                break
        logger.info("Auto Clicker finished.(alt)")

    def click_inf(self, hold_time, delay, timer):
        if self.ui.alt_clk_checkbox.isChecked():
            self.alt_click(hold_time, delay, timer)
            return
        logger.info("Auto Clicker started")
        if self.ui.comboB_mouse_btn.currentText() == "Left":
            down = self.MOUSE_EVENT_LEFTDOWN
            up = self.MOUSE_EVENT_LEFTUP
        elif self.ui.comboB_mouse_btn.currentText() == "Right":
            down = self.MOUSE_EVENT_RIGHTDOWN
            up = self.MOUSE_EVENT_RIGHTUP
        elif self.ui.comboB_mouse_btn.currentText() == "Middle":
            down = self.MOUSE_EVENT_MIDDLEDOWN
            up = self.MOUSE_EVENT_MIDDLEUP
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
                    logger.info("Auto Clicker ended.")
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
                self.ui.btn_shortcut.setDisabled(False)
                logger.info("Auto Clicker ended")
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
        while True:
            self.timer_sleep(
                10
            )  # ? this 10 is in millisecond not second, i found 10 millisecond to be the most accurate
            temp = temp - 0.010
            if self.__stop_threads:
                temp = 0
            if temp <= 0:
                self.__stop_threads = True
                logger.info("Timer ended.")
                break

    def timer_sleep(self, delay):
        target = time.perf_counter_ns() + delay * 1000000
        while time.perf_counter_ns() < target:
            pass  # precise timing

    def start(self):
        if self.click_speed == -1 or self.click_hold == -1 or self.click_timer == -1:
            error_message = "Empty or invalid values when auto clicker started.\nblank fields or non numeric values are not allowed."
            logger.warning(error_message)

            msg_box = QMessageBox()
            msg_box.setWindowTitle("Wrong Values")
            msg_box.setWindowIcon(QIcon(QPixmap(self.icon_name)))
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(error_message)
            msg_box.exec()

        else:
            logger.info("Starting Auto clicker")
            self.ui.btn_shortcut.setDisabled(True)
            self.ui.btn_start.setDisabled(True)
            self.ui.btn_stop.setDisabled(False)
            self.click_thread = threading.Thread(
                target=self.click_inf,
                args=(self.click_hold, self.click_speed, self.click_timer),
            )
            self.__stop_threads = False
            self.click_thread.start()

    def stop(self):
        logger.info("Stopping Auto clicker")
        self.__stop_threads = True
        try:
            self.click_thread.join()
        except RuntimeError:
            logger.warning(
                "clicker thread was running, if the app is working correctly you may ignore this warning."
            )
        self.ui.btn_start.setDisabled(False)
        self.ui.btn_stop.setDisabled(True)
        self.ui.btn_shortcut.setDisabled(False)

    def update_vars(self):
        # ^ main update task
        try:
            self.click_speed = (
                int(self.ui.le_hours.text()) * 3600
                + int(self.ui.le_mins.text()) * 60
                + int(self.ui.le_s.text())
                + int(self.ui.le_ms.text()) / 1000
            )
            self.config["interval"]["hour"] = self.ui.le_hours.text()
            self.config["interval"]["minute"] = self.ui.le_mins.text()
            self.config["interval"]["second"] = self.ui.le_s.text()
            self.config["interval"]["milliseconds"] = self.ui.le_ms.text()
            with open(SETTINGS, "w") as f:
                self.config.write(f)

        except ValueError:
            self.click_speed = -1
            logger.warning(
                "Wrong values for click speed, use different values, this warning is safe."
            )
        try:
            self.click_timer = (
                int(self.ui.le_timer_h.text()) * 3600
                + int(self.ui.le_timer_min.text()) * 60
                + int(self.ui.le_timer_s.text())
                + int(self.ui.le_timer_ms.text()) / 1000
            )
            self.config["timer"]["hour"] = self.ui.le_timer_h.text()
            self.config["timer"]["minute"] = self.ui.le_timer_min.text()
            self.config["timer"]["second"] = self.ui.le_timer_s.text()
            self.config["timer"]["milliseconds"] = self.ui.le_timer_ms.text()
            with open(SETTINGS, "w") as f:
                self.config.write(f)

        except ValueError:
            self.click_timer = -1
            logger.warning(
                "Wrong values for click timer, use different values, this warning is safe."
            )
        try:
            self.click_hold = (
                int(self.ui.le_hold_hours.text()) * 3600
                + int(self.ui.le_hold_mins.text()) * 60
                + int(self.ui.le_hold_s.text())
                + int(self.ui.le_hold_ms.text()) / 1000
            )
            self.config["holdTime"]["hour"] = self.ui.le_hold_hours.text()
            self.config["holdTime"]["minute"] = self.ui.le_hold_mins.text()
            self.config["holdTime"]["second"] = self.ui.le_hold_s.text()
            self.config["holdTime"]["milliseconds"] = self.ui.le_hold_ms.text()
            with open(SETTINGS, "w") as f:
                self.config.write(f)

        except ValueError:
            self.click_hold = -1
            logger.warning(
                "Wrong values for click hold, use different values, this warning is safe."
            )
        self.click_repeat = abs(int(self.ui.repeat_times.text()))
        self.config["repeat"]["repeat-times"] = str(self.click_repeat)
        with open(SETTINGS, "w") as f:
            self.config.write(f)
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

    # & Tray Icon Functions-----
    def closeEvent(self, event):
        if self.ui.tray_icon_visible.isChecked():
            # Minimize to tray instead of closing
            event.ignore()  # Ignore the close event
            self.hide()  # Hide the window
        else:
            event.accept()

    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def restore_window(self):
        self.show()
        self.activateWindow()

    def exit_app(self):
        # self.tray_icon.setVisible(False)  # Hide the tray icon
        QApplication.quit()  # Exit the application

    # & -------------------------

    # & Checkbox functions
    def alt_clk_checkbox_function(self):
        self.config["checkbox"]["alt_click"] = str(self.ui.alt_clk_checkbox.isChecked())
        with open(SETTINGS, "w") as f:
            self.config.write(f)

    def tray_icon_visible_function(self):
        self.config["checkbox"]["tray_icon_visible"] = str(
            self.ui.tray_icon_visible.isChecked()
        )
        with open(SETTINGS, "w") as f:
            self.config.write(f)

        if self.ui.tray_icon_visible.isChecked():
            self.tray_icon.show()
        else:
            self.tray_icon.hide()


def main() -> None:

    # ^ checking if essential folders exist or not, if not create them
    LOGS_PATH = pathlib.Path("logs/")
    if not LOGS_PATH.exists():
        LOGS_PATH.mkdir()

    # ^ logging stuff
    logger.add("logs/log_{time}.log", retention="3 days", level="INFO")

    # ^ main app
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
