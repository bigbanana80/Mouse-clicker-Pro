import pyautogui
import sys
import time
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from mainUi import Ui_main_window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.btn_stop.setDisabled(True)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)

    def click(self, hold_time, repeat, mouse_btn, delay):
        for _ in range(repeat):
            pyautogui.mouseDown(button=mouse_btn)
            time.sleep(hold_time)
            pyautogui.mouseUp(button=mouse_btn)
            time.sleep(delay)

    def start(self):
        self.ui.btn_start.setDisabled(True)
        self.ui.btn_stop.setDisabled(False)
        while self.ui.btn_start.isEnabled == False:
            pyautogui.mouseDown(button="left")
            QtCore.QTimer.start(1000)
            pyautogui.mouseUp(button="left")

    def stop(self):
        self.ui.btn_start.setDisabled(False)
        self.ui.btn_stop.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
