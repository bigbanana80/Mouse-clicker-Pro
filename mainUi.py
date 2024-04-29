# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(601, 583)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setFocusPolicy(Qt.NoFocus)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.grb_clk_interval = QGroupBox(self.central_widget)
        self.grb_clk_interval.setObjectName(u"grb_clk_interval")
        self.grb_clk_interval.setGeometry(QRect(10, 20, 581, 121))
        self.label = QLabel(self.grb_clk_interval)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 30, 49, 16))
        self.label_2 = QLabel(self.grb_clk_interval)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 30, 49, 16))
        self.label_3 = QLabel(self.grb_clk_interval)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 30, 49, 16))
        self.label_4 = QLabel(self.grb_clk_interval)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 30, 71, 16))
        self.le_hours = QLineEdit(self.grb_clk_interval)
        self.le_hours.setObjectName(u"le_hours")
        self.le_hours.setGeometry(QRect(10, 30, 81, 22))
        self.le_mins = QLineEdit(self.grb_clk_interval)
        self.le_mins.setObjectName(u"le_mins")
        self.le_mins.setGeometry(QRect(140, 30, 81, 22))
        self.le_s = QLineEdit(self.grb_clk_interval)
        self.le_s.setObjectName(u"le_s")
        self.le_s.setGeometry(QRect(270, 30, 81, 22))
        self.le_ms = QLineEdit(self.grb_clk_interval)
        self.le_ms.setObjectName(u"le_ms")
        self.le_ms.setGeometry(QRect(400, 30, 81, 22))
        self.grb_clk_settings = QGroupBox(self.central_widget)
        self.grb_clk_settings.setObjectName(u"grb_clk_settings")
        self.grb_clk_settings.setGeometry(QRect(10, 160, 251, 211))
        self.grb_cur_pos = QGroupBox(self.central_widget)
        self.grb_cur_pos.setObjectName(u"grb_cur_pos")
        self.grb_cur_pos.setGeometry(QRect(290, 260, 301, 111))
        self.grb_clk_timer = QGroupBox(self.central_widget)
        self.grb_clk_timer.setObjectName(u"grb_clk_timer")
        self.grb_clk_timer.setGeometry(QRect(290, 160, 301, 91))
        self.btn_start = QPushButton(self.central_widget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(130, 390, 141, 51))
        self.btn_stop = QPushButton(self.central_widget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(290, 390, 141, 51))
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 601, 22))
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName(u"status_bar")
        main_window.setStatusBar(self.status_bar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Auto Clicker Pro", None))
        self.grb_clk_interval.setTitle(QCoreApplication.translate("main_window", u"Click interval", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Hours", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"mins", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"seconds", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"milliseconds", None))
        self.le_hours.setText("")
        self.le_mins.setText("")
        self.le_s.setText("")
        self.le_ms.setText("")
        self.grb_clk_settings.setTitle(QCoreApplication.translate("main_window", u"Click settings", None))
        self.grb_cur_pos.setTitle(QCoreApplication.translate("main_window", u"Cursur Position", None))
        self.grb_clk_timer.setTitle(QCoreApplication.translate("main_window", u"Click Timer", None))
        self.btn_start.setText(QCoreApplication.translate("main_window", u"Start", None))
        self.btn_stop.setText(QCoreApplication.translate("main_window", u"Stop", None))
    # retranslateUi

