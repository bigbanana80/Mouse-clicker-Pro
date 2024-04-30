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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(591, 654)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.grb_clk_interval = QGroupBox(self.central_widget)
        self.grb_clk_interval.setObjectName(u"grb_clk_interval")
        self.grb_clk_interval.setGeometry(QRect(10, 10, 571, 81))
        self.gridLayout_5 = QGridLayout(self.grb_clk_interval)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.le_hours = QLineEdit(self.grb_clk_interval)
        self.le_hours.setObjectName(u"le_hours")

        self.gridLayout_5.addWidget(self.le_hours, 0, 0, 1, 1)

        self.label = QLabel(self.grb_clk_interval)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)

        self.le_mins = QLineEdit(self.grb_clk_interval)
        self.le_mins.setObjectName(u"le_mins")

        self.gridLayout_5.addWidget(self.le_mins, 0, 2, 1, 1)

        self.label_2 = QLabel(self.grb_clk_interval)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 3, 1, 1)

        self.le_s = QLineEdit(self.grb_clk_interval)
        self.le_s.setObjectName(u"le_s")

        self.gridLayout_5.addWidget(self.le_s, 0, 4, 1, 1)

        self.label_3 = QLabel(self.grb_clk_interval)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 5, 1, 1)

        self.le_ms = QLineEdit(self.grb_clk_interval)
        self.le_ms.setObjectName(u"le_ms")

        self.gridLayout_5.addWidget(self.le_ms, 0, 6, 1, 1)

        self.label_4 = QLabel(self.grb_clk_interval)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 7, 1, 1)

        self.grb_clk_settings = QGroupBox(self.central_widget)
        self.grb_clk_settings.setObjectName(u"grb_clk_settings")
        self.grb_clk_settings.setGeometry(QRect(10, 170, 271, 161))
        self.gridLayout = QGridLayout(self.grb_clk_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.grb_clk_settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.comboB_mouse_btn = QComboBox(self.grb_clk_settings)
        self.comboB_mouse_btn.addItem("")
        self.comboB_mouse_btn.addItem("")
        self.comboB_mouse_btn.addItem("")
        self.comboB_mouse_btn.setObjectName(u"comboB_mouse_btn")

        self.gridLayout.addWidget(self.comboB_mouse_btn, 0, 1, 1, 1)

        self.label_6 = QLabel(self.grb_clk_settings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.comboB_clickType = QComboBox(self.grb_clk_settings)
        self.comboB_clickType.addItem("")
        self.comboB_clickType.addItem("")
        self.comboB_clickType.addItem("")
        self.comboB_clickType.addItem("")
        self.comboB_clickType.setObjectName(u"comboB_clickType")

        self.gridLayout.addWidget(self.comboB_clickType, 1, 1, 1, 1)

        self.grb_cur_pos = QGroupBox(self.central_widget)
        self.grb_cur_pos.setObjectName(u"grb_cur_pos")
        self.grb_cur_pos.setGeometry(QRect(290, 330, 291, 121))
        self.gridLayout_3 = QGridLayout(self.grb_cur_pos)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pos_opt_1 = QRadioButton(self.grb_cur_pos)
        self.pos_opt_1.setObjectName(u"pos_opt_1")
        self.pos_opt_1.setChecked(True)

        self.gridLayout_3.addWidget(self.pos_opt_1, 0, 0, 1, 3)

        self.pos_opt_2 = QRadioButton(self.grb_cur_pos)
        self.pos_opt_2.setObjectName(u"pos_opt_2")

        self.gridLayout_3.addWidget(self.pos_opt_2, 1, 0, 1, 1)

        self.label_11 = QLabel(self.grb_cur_pos)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.grb_cur_pos)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_12 = QLabel(self.grb_cur_pos)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.grb_cur_pos)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 4, 1, 1)

        self.btn_start = QPushButton(self.central_widget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(140, 460, 141, 51))
        self.btn_stop = QPushButton(self.central_widget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)
        self.btn_stop.setGeometry(QRect(290, 460, 141, 51))
        self.grb_clk_repeat = QGroupBox(self.central_widget)
        self.grb_clk_repeat.setObjectName(u"grb_clk_repeat")
        self.grb_clk_repeat.setGeometry(QRect(10, 330, 271, 121))
        self.gridLayout_4 = QGridLayout(self.grb_clk_repeat)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.repeat_opt_1 = QRadioButton(self.grb_clk_repeat)
        self.repeat_opt_1.setObjectName(u"repeat_opt_1")

        self.gridLayout_4.addWidget(self.repeat_opt_1, 0, 0, 1, 1)

        self.repeat_times = QSpinBox(self.grb_clk_repeat)
        self.repeat_times.setObjectName(u"repeat_times")
        self.repeat_times.setEnabled(False)

        self.gridLayout_4.addWidget(self.repeat_times, 0, 1, 1, 1)

        self.repeat_opt_2 = QRadioButton(self.grb_clk_repeat)
        self.repeat_opt_2.setObjectName(u"repeat_opt_2")
        self.repeat_opt_2.setChecked(True)

        self.gridLayout_4.addWidget(self.repeat_opt_2, 1, 0, 1, 2)

        self.grb_clk_timer = QGroupBox(self.central_widget)
        self.grb_clk_timer.setObjectName(u"grb_clk_timer")
        self.grb_clk_timer.setGeometry(QRect(290, 170, 291, 161))
        self.gridLayout_2 = QGridLayout(self.grb_clk_timer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.grb_clk_timer)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.le_timer_h = QLineEdit(self.grb_clk_timer)
        self.le_timer_h.setObjectName(u"le_timer_h")

        self.gridLayout_2.addWidget(self.le_timer_h, 0, 1, 1, 1)

        self.label_7 = QLabel(self.grb_clk_timer)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.le_timer_min = QLineEdit(self.grb_clk_timer)
        self.le_timer_min.setObjectName(u"le_timer_min")

        self.gridLayout_2.addWidget(self.le_timer_min, 0, 3, 1, 1)

        self.label_10 = QLabel(self.grb_clk_timer)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.le_timer_s = QLineEdit(self.grb_clk_timer)
        self.le_timer_s.setObjectName(u"le_timer_s")

        self.gridLayout_2.addWidget(self.le_timer_s, 1, 1, 1, 1)

        self.label_8 = QLabel(self.grb_clk_timer)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.le_timer_ms = QLineEdit(self.grb_clk_timer)
        self.le_timer_ms.setObjectName(u"le_timer_ms")

        self.gridLayout_2.addWidget(self.le_timer_ms, 1, 3, 1, 1)

        self.grb_clk_interval_2 = QGroupBox(self.central_widget)
        self.grb_clk_interval_2.setObjectName(u"grb_clk_interval_2")
        self.grb_clk_interval_2.setGeometry(QRect(10, 90, 571, 81))
        self.gridLayout_6 = QGridLayout(self.grb_clk_interval_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.le_hold_hours = QLineEdit(self.grb_clk_interval_2)
        self.le_hold_hours.setObjectName(u"le_hold_hours")

        self.gridLayout_6.addWidget(self.le_hold_hours, 0, 0, 1, 1)

        self.label_13 = QLabel(self.grb_clk_interval_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 1, 1, 1)

        self.le_hold_mins = QLineEdit(self.grb_clk_interval_2)
        self.le_hold_mins.setObjectName(u"le_hold_mins")

        self.gridLayout_6.addWidget(self.le_hold_mins, 0, 2, 1, 1)

        self.label_14 = QLabel(self.grb_clk_interval_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 3, 1, 1)

        self.le_hold_s = QLineEdit(self.grb_clk_interval_2)
        self.le_hold_s.setObjectName(u"le_hold_s")

        self.gridLayout_6.addWidget(self.le_hold_s, 0, 4, 1, 1)

        self.label_15 = QLabel(self.grb_clk_interval_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 0, 5, 1, 1)

        self.le_hold_ms = QLineEdit(self.grb_clk_interval_2)
        self.le_hold_ms.setObjectName(u"le_hold_ms")

        self.gridLayout_6.addWidget(self.le_hold_ms, 0, 6, 1, 1)

        self.label_16 = QLabel(self.grb_clk_interval_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 0, 7, 1, 1)

        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 591, 22))
        main_window.setMenuBar(self.menu_bar)
        self.statusBar = QStatusBar(main_window)
        self.statusBar.setObjectName(u"statusBar")
        main_window.setStatusBar(self.statusBar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Auto Clicker Pro", None))
#if QT_CONFIG(tooltip)
        self.grb_clk_interval.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Control how fast the auto clicker works. ( 100 milliseconds is the default speed which is 10 clicks per seconds)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.grb_clk_interval.setWhatsThis(QCoreApplication.translate("main_window", u"<html><head/><body><p>Control how fast the auto clicker works. ( 100 milliseconds is the default speed which is 10 clicks per seconds)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.grb_clk_interval.setTitle(QCoreApplication.translate("main_window", u"Click interval", None))
        self.le_hours.setText("")
        self.label.setText(QCoreApplication.translate("main_window", u"Hours", None))
        self.le_mins.setText("")
        self.label_2.setText(QCoreApplication.translate("main_window", u"mins", None))
        self.le_s.setText("")
        self.label_3.setText(QCoreApplication.translate("main_window", u"seconds", None))
        self.le_ms.setText("")
        self.label_4.setText(QCoreApplication.translate("main_window", u"milliseconds", None))
#if QT_CONFIG(tooltip)
        self.grb_clk_settings.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Controls the click type and the mouse button that will perform the click.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.grb_clk_settings.setTitle(QCoreApplication.translate("main_window", u"Click settings", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"Mouse button :", None))
        self.comboB_mouse_btn.setItemText(0, QCoreApplication.translate("main_window", u"Left", None))
        self.comboB_mouse_btn.setItemText(1, QCoreApplication.translate("main_window", u"Right", None))
        self.comboB_mouse_btn.setItemText(2, QCoreApplication.translate("main_window", u"Middle", None))

        self.label_6.setText(QCoreApplication.translate("main_window", u"Click Type :", None))
        self.comboB_clickType.setItemText(0, QCoreApplication.translate("main_window", u"Single", None))
        self.comboB_clickType.setItemText(1, QCoreApplication.translate("main_window", u"Double", None))
        self.comboB_clickType.setItemText(2, QCoreApplication.translate("main_window", u"Triple", None))
        self.comboB_clickType.setItemText(3, QCoreApplication.translate("main_window", u"Hold", None))

#if QT_CONFIG(tooltip)
        self.grb_cur_pos.setToolTip(QCoreApplication.translate("main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Controls the position of the cursur, by default it clicks on the current position of the cursur and you are able to move the cursur around. specifying a  position means the auto clicker will only click that position on the screen which varies depending on the monitor.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.grb_cur_pos.setTitle(QCoreApplication.translate("main_window", u"Cursur Position", None))
        self.pos_opt_1.setText(QCoreApplication.translate("main_window", u"Current position (default)", None))
        self.pos_opt_2.setText(QCoreApplication.translate("main_window", u"Pick position :", None))
        self.label_11.setText(QCoreApplication.translate("main_window", u"X :", None))
        self.lineEdit.setText("")
        self.label_12.setText(QCoreApplication.translate("main_window", u"Y :", None))
        self.lineEdit_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_start.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Starts the auto clicker. (default shortcut is F6)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start.setText(QCoreApplication.translate("main_window", u"Start", None))
#if QT_CONFIG(tooltip)
        self.btn_stop.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>stops the auto clicker. (default shortcut is F6)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_stop.setText(QCoreApplication.translate("main_window", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.grb_clk_repeat.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>how much clicks  the auto clicker will perform.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.grb_clk_repeat.setTitle(QCoreApplication.translate("main_window", u"Click Repeat", None))
        self.repeat_opt_1.setText(QCoreApplication.translate("main_window", u"Repeat", None))
        self.repeat_opt_2.setText(QCoreApplication.translate("main_window", u"Click until stopped .", None))
#if QT_CONFIG(tooltip)
        self.grb_clk_timer.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>How long the auto clicker will work. (0 on all time slots means no time limit)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.grb_clk_timer.setTitle(QCoreApplication.translate("main_window", u"Click Timer", None))
        self.label_9.setText(QCoreApplication.translate("main_window", u"Hours", None))
        self.label_7.setText(QCoreApplication.translate("main_window", u"min", None))
        self.label_10.setText(QCoreApplication.translate("main_window", u"seconds", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"milliseconds", None))
#if QT_CONFIG(tooltip)
        self.grb_clk_interval_2.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Controls how long the mouse will hold to button as if it didnt let go of the click before releasing it. ( some games could use this function)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.grb_clk_interval_2.setWhatsThis(QCoreApplication.translate("main_window", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.grb_clk_interval_2.setTitle(QCoreApplication.translate("main_window", u"Click hold time", None))
        self.le_hold_hours.setText("")
        self.label_13.setText(QCoreApplication.translate("main_window", u"Hours", None))
        self.le_hold_mins.setText("")
        self.label_14.setText(QCoreApplication.translate("main_window", u"mins", None))
        self.le_hold_s.setText("")
        self.label_15.setText(QCoreApplication.translate("main_window", u"seconds", None))
        self.le_hold_ms.setText("")
        self.label_16.setText(QCoreApplication.translate("main_window", u"milliseconds", None))
    # retranslateUi

