import pyautogui
import sys
import time
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from mainUi import Ui_main_window
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()

        self.__stop_threads = True
        self.click_thread = threading.Thread(target=self.click_inf, args=(1, "left", 2))

        self.ui.btn_stop.setDisabled(True)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)

    def click_inf(self, hold_time, mouse_btn, delay):
        while True:
            pyautogui.mouseDown(button=mouse_btn)
            self.timer.start(hold_time * 1000)
            pyautogui.mouseUp(button=mouse_btn)
            self.timer.start(delay * 1000)
            if self.__stop_threads == True:
                break

    def start(self):
        self.ui.btn_start.setDisabled(True)
        self.ui.btn_stop.setDisabled(False)
        self.__stop_threads = False
        self.click_thread.start()

    def stop(self):
        self.__stop_threads = True
        self.click_thread.join()
        self.ui.btn_start.setDisabled(False)
        self.ui.btn_stop.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
