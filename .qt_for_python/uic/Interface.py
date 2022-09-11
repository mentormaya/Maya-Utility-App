# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

from widgets.DropZone import DropZone
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        icon = QIcon()
        icon.addFile(u"../../../../.designer/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"border-radius: 10;\n"
"color: rgb(255,255,255)")
        self.verticalLayout_26 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 0, 0, 0)
        self.app_title = QLabel(self.frame_title)
        self.app_title.setObjectName(u"app_title")
        font1 = QFont()
        font1.setFamilies([u"Helvetica"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.app_title.setFont(font1)
        self.app_title.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.app_title, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_title, 0, Qt.AlignVCenter)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(150, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 146, 73);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 146, 73, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 62, 62);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 62, 62, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.title_bar)

        self.contents = QFrame(self.drop_shadow_frame)
        self.contents.setObjectName(u"contents")
        self.contents.setStyleSheet(u"background-color:none;")
        self.contents.setFrameShape(QFrame.NoFrame)
        self.contents.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.contents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.app_info_frame = QFrame(self.contents)
        self.app_info_frame.setObjectName(u"app_info_frame")
        self.app_info_frame.setMinimumSize(QSize(0, 150))
        self.app_info_frame.setMaximumSize(QSize(16777215, 150))
        self.app_info_frame.setStyleSheet(u"border-radius: 0px;\n"
"border-top: 1px solid rgb(133, 133, 133);")
        self.app_info_frame.setFrameShape(QFrame.NoFrame)
        self.app_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.app_info_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settings_menu = QPushButton(self.app_info_frame)
        self.settings_menu.setObjectName(u"settings_menu")
        font2 = QFont()
        font2.setBold(True)
        self.settings_menu.setFont(font2)
        self.settings_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_menu.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.settings_menu)

        self.help_menu = QPushButton(self.app_info_frame)
        self.help_menu.setObjectName(u"help_menu")
        self.help_menu.setFont(font2)
        self.help_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.help_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_menu.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.help_menu)

        self.about_menu = QPushButton(self.app_info_frame)
        self.about_menu.setObjectName(u"about_menu")
        self.about_menu.setFont(font2)
        self.about_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_menu.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.about_menu)


        self.gridLayout.addWidget(self.app_info_frame, 2, 0, 1, 1)

        self.top_bar_frame = QFrame(self.contents)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setStyleSheet(u"background-color: rgb(37, 37, 38);\n"
"padding: 2px;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.welcome_text = QFrame(self.top_bar_frame)
        self.welcome_text.setObjectName(u"welcome_text")
        font3 = QFont()
        font3.setPointSize(2)
        self.welcome_text.setFont(font3)
        self.welcome_text.setFrameShape(QFrame.NoFrame)
        self.welcome_text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.welcome_text)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.welcome_label = QLabel(self.welcome_text)
        self.welcome_label.setObjectName(u"welcome_label")
        font4 = QFont()
        font4.setFamilies([u"Helvetica"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.welcome_label.setFont(font4)

        self.verticalLayout_3.addWidget(self.welcome_label, 0, Qt.AlignBottom)

        self.quotes_label = QLabel(self.welcome_text)
        self.quotes_label.setObjectName(u"quotes_label")
        self.quotes_label.setMinimumSize(QSize(0, 0))
        self.quotes_label.setMaximumSize(QSize(500, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Kalam Light"])
        font5.setPointSize(10)
        font5.setItalic(False)
        self.quotes_label.setFont(font5)
        self.quotes_label.setScaledContents(True)
        self.quotes_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.quotes_label, 0, Qt.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.welcome_text)

        self.date_frame = QFrame(self.top_bar_frame)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.date_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.date_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.dates_grid = QGridLayout(self.groupBox)
        self.dates_grid.setObjectName(u"dates_grid")
        self.nepali_date = QLabel(self.groupBox)
        self.nepali_date.setObjectName(u"nepali_date")
        font6 = QFont()
        font6.setFamilies([u"MS Sans Serif"])
        font6.setPointSize(14)
        self.nepali_date.setFont(font6)
        self.nepali_date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.dates_grid.addWidget(self.nepali_date, 0, 0, 1, 1)

        self.intdt_copy_btn = QPushButton(self.groupBox)
        self.intdt_copy_btn.setObjectName(u"intdt_copy_btn")
        self.intdt_copy_btn.setMinimumSize(QSize(25, 0))
        self.intdt_copy_btn.setMaximumSize(QSize(25, 16777215))
        self.intdt_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.intdt_copy_btn.setIcon(icon4)

        self.dates_grid.addWidget(self.intdt_copy_btn, 1, 1, 1, 1, Qt.AlignLeft)

        self.int_date = QLabel(self.groupBox)
        self.int_date.setObjectName(u"int_date")
        self.int_date.setFont(font6)
        self.int_date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.dates_grid.addWidget(self.int_date, 1, 0, 1, 1)

        self.npdt_copy_btn = QPushButton(self.groupBox)
        self.npdt_copy_btn.setObjectName(u"npdt_copy_btn")
        self.npdt_copy_btn.setMinimumSize(QSize(25, 0))
        self.npdt_copy_btn.setMaximumSize(QSize(25, 16777215))
        self.npdt_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.npdt_copy_btn.setIcon(icon4)

        self.dates_grid.addWidget(self.npdt_copy_btn, 0, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox)


        self.horizontalLayout_6.addWidget(self.date_frame)

        self.top_right_menu = QFrame(self.top_bar_frame)
        self.top_right_menu.setObjectName(u"top_right_menu")
        self.top_right_menu.setMinimumSize(QSize(150, 0))
        self.top_right_menu.setMaximumSize(QSize(150, 16777215))
        self.top_right_menu.setFrameShape(QFrame.StyledPanel)
        self.top_right_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.top_right_menu)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.np_cal_btn = QPushButton(self.top_right_menu)
        self.np_cal_btn.setObjectName(u"np_cal_btn")
        self.np_cal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.np_cal_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.np_cal_btn.setIcon(icon5)

        self.horizontalLayout_8.addWidget(self.np_cal_btn)

        self.options_btn = QPushButton(self.top_right_menu)
        self.options_btn.setObjectName(u"options_btn")
        self.options_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.options_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        self.options_btn.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.options_btn)


        self.horizontalLayout_6.addWidget(self.top_right_menu)


        self.gridLayout.addWidget(self.top_bar_frame, 0, 1, 1, 2)

        self.content_frame = QFrame(self.contents)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"border-radius: 0px;")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.main_content_pages = QStackedWidget(self.content_frame)
        self.main_content_pages.setObjectName(u"main_content_pages")
        font7 = QFont()
        font7.setItalic(False)
        self.main_content_pages.setFont(font7)
        self.main_content_pages.setStyleSheet(u"\n"
"QLineEdit{\n"
"	border: none;\n"
"	border-Bottom: 2px solid #5e5e5e;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-Bottom: 2px solid #7e7e7e;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-Bottom: 2px solid #7e7e7e;\n"
"}")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_8 = QVBoxLayout(self.dashboard)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.dashboard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.main_content_pages.addWidget(self.dashboard)
        self.utilites_number = QWidget()
        self.utilites_number.setObjectName(u"utilites_number")
        self.verticalLayout_10 = QVBoxLayout(self.utilites_number)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.input_number = QFrame(self.utilites_number)
        self.input_number.setObjectName(u"input_number")
        self.input_number.setMinimumSize(QSize(0, 40))
        self.input_number.setMaximumSize(QSize(16777215, 60))
        self.input_number.setStyleSheet(u"QFrame{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"")
        self.input_number.setFrameShape(QFrame.StyledPanel)
        self.input_number.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.input_number)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.number_input_label = QLabel(self.input_number)
        self.number_input_label.setObjectName(u"number_input_label")
        font8 = QFont()
        font8.setFamilies([u"Helvetica"])
        font8.setPointSize(12)
        self.number_input_label.setFont(font8)

        self.horizontalLayout_9.addWidget(self.number_input_label)

        self.num_input = QLineEdit(self.input_number)
        self.num_input.setObjectName(u"num_input")
        font9 = QFont()
        font9.setFamilies([u"Helvetica"])
        font9.setPointSize(12)
        font9.setItalic(True)
        self.num_input.setFont(font9)
        self.num_input.setAutoFillBackground(False)
        self.num_input.setStyleSheet(u"")
        self.num_input.setPlaceholderText(u"Number to Convert")
        self.num_input.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.num_input)

        self.clear_btn = QPushButton(self.input_number)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon6)

        self.horizontalLayout_9.addWidget(self.clear_btn)

        self.copy_num_all_btn = QPushButton(self.input_number)
        self.copy_num_all_btn.setObjectName(u"copy_num_all_btn")
        self.copy_num_all_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_num_all_btn.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.copy_num_all_btn)

        self.convert_btn = QPushButton(self.input_number)
        self.convert_btn.setObjectName(u"convert_btn")
        self.convert_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	background-color: rgba(152, 152, 151, 200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 4px;\n"
"	background-color: rgba(152, 152, 151, 150);\n"
"}")

        self.horizontalLayout_9.addWidget(self.convert_btn)


        self.verticalLayout_10.addWidget(self.input_number)

        self.output_number = QFrame(self.utilites_number)
        self.output_number.setObjectName(u"output_number")
        self.output_number.setStyleSheet(u"QLineEdit{\n"
"	border:none;\n"
"}")
        self.output_number.setFrameShape(QFrame.StyledPanel)
        self.output_number.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.output_number)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.number_output = QGridLayout()
        self.number_output.setObjectName(u"number_output")
        self.number_output.setHorizontalSpacing(10)
        self.number_output.setContentsMargins(10, 10, 10, 10)
        self.decimal_lbl = QLabel(self.output_number)
        self.decimal_lbl.setObjectName(u"decimal_lbl")
        self.decimal_lbl.setFont(font8)

        self.number_output.addWidget(self.decimal_lbl, 3, 0, 1, 1)

        self.eng_lbl = QLabel(self.output_number)
        self.eng_lbl.setObjectName(u"eng_lbl")
        self.eng_lbl.setFont(font8)

        self.number_output.addWidget(self.eng_lbl, 1, 0, 1, 1)

        self.nep_words_copy_btn = QPushButton(self.output_number)
        self.nep_words_copy_btn.setObjectName(u"nep_words_copy_btn")
        font10 = QFont()
        font10.setPointSize(8)
        self.nep_words_copy_btn.setFont(font10)
        self.nep_words_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nep_words_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.nep_words_copy_btn, 8, 2, 1, 1)

        self.nepali_disp = QLineEdit(self.output_number)
        self.nepali_disp.setObjectName(u"nepali_disp")
        self.nepali_disp.setEnabled(False)
        self.nepali_disp.setFont(font8)

        self.number_output.addWidget(self.nepali_disp, 2, 1, 1, 1)

        self.whole_lbl = QLabel(self.output_number)
        self.whole_lbl.setObjectName(u"whole_lbl")
        self.whole_lbl.setFont(font8)

        self.number_output.addWidget(self.whole_lbl, 4, 0, 1, 1)

        self.lakh_copy_btn = QPushButton(self.output_number)
        self.lakh_copy_btn.setObjectName(u"lakh_copy_btn")
        self.lakh_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lakh_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.lakh_copy_btn, 5, 2, 1, 1)

        self.num_copy_btn = QPushButton(self.output_number)
        self.num_copy_btn.setObjectName(u"num_copy_btn")
        self.num_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.num_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.num_copy_btn, 0, 2, 1, 1)

        self.words_nep_disp = QLabel(self.output_number)
        self.words_nep_disp.setObjectName(u"words_nep_disp")
        self.words_nep_disp.setFont(font8)
        self.words_nep_disp.setWordWrap(True)

        self.number_output.addWidget(self.words_nep_disp, 8, 1, 1, 1)

        self.words_nep_lbl = QLabel(self.output_number)
        self.words_nep_lbl.setObjectName(u"words_nep_lbl")
        self.words_nep_lbl.setFont(font8)

        self.number_output.addWidget(self.words_nep_lbl, 8, 0, 1, 1)

        self.nep_copy_btn = QPushButton(self.output_number)
        self.nep_copy_btn.setObjectName(u"nep_copy_btn")
        self.nep_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nep_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.nep_copy_btn, 2, 2, 1, 1)

        self.lakh_lbl = QLabel(self.output_number)
        self.lakh_lbl.setObjectName(u"lakh_lbl")
        self.lakh_lbl.setFont(font8)

        self.number_output.addWidget(self.lakh_lbl, 5, 0, 1, 1)

        self.nepali_lbl = QLabel(self.output_number)
        self.nepali_lbl.setObjectName(u"nepali_lbl")
        self.nepali_lbl.setFont(font8)

        self.number_output.addWidget(self.nepali_lbl, 2, 0, 1, 1)

        self.number_disp = QLineEdit(self.output_number)
        self.number_disp.setObjectName(u"number_disp")
        self.number_disp.setEnabled(False)
        self.number_disp.setFont(font8)

        self.number_output.addWidget(self.number_disp, 0, 1, 1, 1)

        self.num_lbl = QLabel(self.output_number)
        self.num_lbl.setObjectName(u"num_lbl")
        self.num_lbl.setFont(font8)

        self.number_output.addWidget(self.num_lbl, 0, 0, 1, 1)

        self.decimal_disp = QLineEdit(self.output_number)
        self.decimal_disp.setObjectName(u"decimal_disp")
        self.decimal_disp.setEnabled(False)
        self.decimal_disp.setFont(font8)

        self.number_output.addWidget(self.decimal_disp, 3, 1, 1, 1)

        self.eng_words_copy_btn = QPushButton(self.output_number)
        self.eng_words_copy_btn.setObjectName(u"eng_words_copy_btn")
        self.eng_words_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eng_words_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.eng_words_copy_btn, 7, 2, 1, 1)

        self.words_eng_lbl = QLabel(self.output_number)
        self.words_eng_lbl.setObjectName(u"words_eng_lbl")
        self.words_eng_lbl.setFont(font8)

        self.number_output.addWidget(self.words_eng_lbl, 7, 0, 1, 1)

        self.whole_disp = QLineEdit(self.output_number)
        self.whole_disp.setObjectName(u"whole_disp")
        self.whole_disp.setEnabled(False)
        self.whole_disp.setFont(font8)

        self.number_output.addWidget(self.whole_disp, 4, 1, 1, 1)

        self.million_lbl = QLabel(self.output_number)
        self.million_lbl.setObjectName(u"million_lbl")
        self.million_lbl.setFont(font8)

        self.number_output.addWidget(self.million_lbl, 6, 0, 1, 1)

        self.whole_copy_btn = QPushButton(self.output_number)
        self.whole_copy_btn.setObjectName(u"whole_copy_btn")
        self.whole_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.whole_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.whole_copy_btn, 4, 2, 1, 1)

        self.words_eng_disp = QLabel(self.output_number)
        self.words_eng_disp.setObjectName(u"words_eng_disp")
        self.words_eng_disp.setFont(font8)
        self.words_eng_disp.setWordWrap(True)

        self.number_output.addWidget(self.words_eng_disp, 7, 1, 1, 1)

        self.lakh_format_disp = QLineEdit(self.output_number)
        self.lakh_format_disp.setObjectName(u"lakh_format_disp")
        self.lakh_format_disp.setEnabled(False)
        self.lakh_format_disp.setFont(font8)

        self.number_output.addWidget(self.lakh_format_disp, 5, 1, 1, 1)

        self.million_format_disp = QLineEdit(self.output_number)
        self.million_format_disp.setObjectName(u"million_format_disp")
        self.million_format_disp.setEnabled(False)
        self.million_format_disp.setFont(font8)

        self.number_output.addWidget(self.million_format_disp, 6, 1, 1, 1)

        self.eng_copy_btn = QPushButton(self.output_number)
        self.eng_copy_btn.setObjectName(u"eng_copy_btn")
        self.eng_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eng_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.eng_copy_btn, 1, 2, 1, 1)

        self.million_copy_btn = QPushButton(self.output_number)
        self.million_copy_btn.setObjectName(u"million_copy_btn")
        self.million_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.million_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.million_copy_btn, 6, 2, 1, 1)

        self.decimal_copy_btn = QPushButton(self.output_number)
        self.decimal_copy_btn.setObjectName(u"decimal_copy_btn")
        self.decimal_copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.decimal_copy_btn.setIcon(icon4)

        self.number_output.addWidget(self.decimal_copy_btn, 3, 2, 1, 1)

        self.english_disp = QLineEdit(self.output_number)
        self.english_disp.setObjectName(u"english_disp")
        self.english_disp.setEnabled(False)
        self.english_disp.setFont(font8)

        self.number_output.addWidget(self.english_disp, 1, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.number_output)


        self.verticalLayout_10.addWidget(self.output_number, 0, Qt.AlignTop)

        self.main_content_pages.addWidget(self.utilites_number)
        self.join_pdf_container = QWidget()
        self.join_pdf_container.setObjectName(u"join_pdf_container")
        self.verticalLayout_22 = QVBoxLayout(self.join_pdf_container)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pdf_merger_output = QFrame(self.join_pdf_container)
        self.pdf_merger_output.setObjectName(u"pdf_merger_output")
        self.pdf_merger_output.setFrameShape(QFrame.StyledPanel)
        self.pdf_merger_output.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.pdf_merger_output)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.verticalLayout_22.addWidget(self.pdf_merger_output)

        self.files_input_pdf_merger = QFrame(self.join_pdf_container)
        self.files_input_pdf_merger.setObjectName(u"files_input_pdf_merger")
        self.files_input_pdf_merger.setMinimumSize(QSize(0, 40))
        self.files_input_pdf_merger.setMaximumSize(QSize(16777215, 60))
        self.files_input_pdf_merger.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	background-color: rgba(152, 152, 151, 200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 4px;\n"
"	background-color: rgba(152, 152, 151, 150);\n"
"}")
        self.files_input_pdf_merger.setFrameShape(QFrame.StyledPanel)
        self.files_input_pdf_merger.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.files_input_pdf_merger)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.add_pdf_files_btn = QPushButton(self.files_input_pdf_merger)
        self.add_pdf_files_btn.setObjectName(u"add_pdf_files_btn")
        self.add_pdf_files_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_pdf_files_btn.setIcon(icon7)

        self.horizontalLayout_12.addWidget(self.add_pdf_files_btn)

        self.remove_pdf_file_btn = QPushButton(self.files_input_pdf_merger)
        self.remove_pdf_file_btn.setObjectName(u"remove_pdf_file_btn")
        self.remove_pdf_file_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/file-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_pdf_file_btn.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.remove_pdf_file_btn)

        self.clear_pdf_btn = QPushButton(self.files_input_pdf_merger)
        self.clear_pdf_btn.setObjectName(u"clear_pdf_btn")
        self.clear_pdf_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_pdf_btn.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.clear_pdf_btn)

        self.pdf_move_up_btn = QPushButton(self.files_input_pdf_merger)
        self.pdf_move_up_btn.setObjectName(u"pdf_move_up_btn")
        self.pdf_move_up_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/chevrons-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pdf_move_up_btn.setIcon(icon10)

        self.horizontalLayout_12.addWidget(self.pdf_move_up_btn)

        self.pdf_move_down_btn = QPushButton(self.files_input_pdf_merger)
        self.pdf_move_down_btn.setObjectName(u"pdf_move_down_btn")
        self.pdf_move_down_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pdf_move_down_btn.setIcon(icon11)

        self.horizontalLayout_12.addWidget(self.pdf_move_down_btn)

        self.save_pdf_btn = QPushButton(self.files_input_pdf_merger)
        self.save_pdf_btn.setObjectName(u"save_pdf_btn")
        self.save_pdf_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_pdf_btn.setIcon(icon12)

        self.horizontalLayout_12.addWidget(self.save_pdf_btn)


        self.verticalLayout_22.addWidget(self.files_input_pdf_merger)

        self.main_content_pages.addWidget(self.join_pdf_container)
        self.image_text_extraction_page = DropZone()
        self.image_text_extraction_page.setObjectName(u"image_text_extraction_page")
        self.image_text_extraction_page.setCursor(QCursor(Qt.ArrowCursor))
        self.image_text_extraction_page.setMouseTracking(False)
        self.verticalLayout_221 = QVBoxLayout(self.image_text_extraction_page)
        self.verticalLayout_221.setSpacing(0)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.image_drop_zone = QFrame(self.image_text_extraction_page)
        self.image_drop_zone.setObjectName(u"image_drop_zone")
        self.image_drop_zone.setMinimumSize(QSize(0, 40))
        self.image_drop_zone.setMaximumSize(QSize(16777215, 16777215))
        self.image_drop_zone.setCursor(QCursor(Qt.OpenHandCursor))
        self.image_drop_zone.setStyleSheet(u"QPushButton{\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	background-color: rgba(152, 152, 151, 200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 4px;\n"
"	background-color: rgba(152, 152, 151, 150);\n"
"}")
        self.image_drop_zone.setFrameShape(QFrame.StyledPanel)
        self.image_drop_zone.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.image_drop_zone)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(15, 15, 15, 15)
        self.image_drop_border = QFrame(self.image_drop_zone)
        self.image_drop_border.setObjectName(u"image_drop_border")
        self.image_drop_border.setCursor(QCursor(Qt.ArrowCursor))
        self.image_drop_border.setAcceptDrops(True)
        self.image_drop_border.setStyleSheet(u"QFrame{\n"
"	border: 2px dashed  rgb(125, 125, 124);\n"
"	border-radius: 4px;\n"
"}")
        self.image_drop_border.setFrameShape(QFrame.StyledPanel)
        self.image_drop_border.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.image_drop_border)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.select_file_btn = QPushButton(self.image_drop_border)
        self.select_file_btn.setObjectName(u"select_file_btn")
        self.select_file_btn.setMinimumSize(QSize(150, 0))
        self.select_file_btn.setMaximumSize(QSize(250, 16777215))
        self.select_file_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.select_file_btn)

        self.Image_Label = QLabel(self.image_drop_border)
        self.Image_Label.setObjectName(u"Image_Label")

        self.horizontalLayout_11.addWidget(self.Image_Label, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.image_drop_border)


        self.verticalLayout_221.addWidget(self.image_drop_zone)

        self.text_extracted_disp = QFrame(self.image_text_extraction_page)
        self.text_extracted_disp.setObjectName(u"text_extracted_disp")
        self.text_extracted_disp.setFrameShape(QFrame.StyledPanel)
        self.text_extracted_disp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_231 = QVBoxLayout(self.text_extracted_disp)
        self.verticalLayout_231.setObjectName(u"verticalLayout_231")
        self.extracted_texts = QTextBrowser(self.text_extracted_disp)
        self.extracted_texts.setObjectName(u"extracted_texts")
        self.extracted_texts.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.extracted_texts.setReadOnly(False)

        self.verticalLayout_231.addWidget(self.extracted_texts)


        self.verticalLayout_221.addWidget(self.text_extracted_disp)

        self.main_content_pages.addWidget(self.image_text_extraction_page)
        self.tax_pan_search = QWidget()
        self.tax_pan_search.setObjectName(u"tax_pan_search")
        self.verticalLayout_20 = QVBoxLayout(self.tax_pan_search)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pan_input_container = QFrame(self.tax_pan_search)
        self.pan_input_container.setObjectName(u"pan_input_container")
        self.pan_input_container.setMinimumSize(QSize(0, 40))
        self.pan_input_container.setMaximumSize(QSize(16777215, 60))
        self.pan_input_container.setFrameShape(QFrame.StyledPanel)
        self.pan_input_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.pan_input_container)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pan_input_label = QLabel(self.pan_input_container)
        self.pan_input_label.setObjectName(u"pan_input_label")
        self.pan_input_label.setFont(font8)

        self.horizontalLayout_10.addWidget(self.pan_input_label)

        self.pan_input = QLineEdit(self.pan_input_container)
        self.pan_input.setObjectName(u"pan_input")
        self.pan_input.setFont(font8)
        self.pan_input.setAutoFillBackground(False)
        self.pan_input.setStyleSheet(u"")
        self.pan_input.setPlaceholderText(u"")
        self.pan_input.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.pan_input)

        self.clear_pan_btn = QPushButton(self.pan_input_container)
        self.clear_pan_btn.setObjectName(u"clear_pan_btn")
        self.clear_pan_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_pan_btn.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.clear_pan_btn)

        self.copy_pan_raw_btn = QPushButton(self.pan_input_container)
        self.copy_pan_raw_btn.setObjectName(u"copy_pan_raw_btn")
        self.copy_pan_raw_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_pan_raw_btn.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.copy_pan_raw_btn)

        self.pan_search_btn = QPushButton(self.pan_input_container)
        self.pan_search_btn.setObjectName(u"pan_search_btn")
        self.pan_search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pan_search_btn.setStyleSheet(u"padding: 10px;\n"
"border-radius: 8px;\n"
"background-color: rgb(152, 152, 151);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pan_search_btn.setIcon(icon13)

        self.horizontalLayout_10.addWidget(self.pan_search_btn)


        self.verticalLayout_20.addWidget(self.pan_input_container)

        self.pan_output = QTabWidget(self.tax_pan_search)
        self.pan_output.setObjectName(u"pan_output")
        self.pan_output.setCursor(QCursor(Qt.PointingHandCursor))
        self.pan_output.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid rgb(51, 51, 51);\n"
"  	padding: 2px;\n"
"	background-color: rgba(51, 51, 51,200);\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"	background-color: rgba(47, 47, 47,200);\n"
" 	border: 1px solid rgb(51, 51, 51);\n"
"	padding: 10px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"   background-color: rgba(47, 47, 47,150);\n"
"  margin-bottom: -1px; \n"
"}\n"
"\n"
"QTabBar::tab:hover { \n"
"   background-color: rgba(47, 47, 47,150);\n"
"}")
        self.pan_table_output_page = QWidget()
        self.pan_table_output_page.setObjectName(u"pan_table_output_page")
        self.verticalLayout_27 = QVBoxLayout(self.pan_table_output_page)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pan_table_output = QTableWidget(self.pan_table_output_page)
        if (self.pan_table_output.columnCount() < 1):
            self.pan_table_output.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.pan_table_output.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.pan_table_output.rowCount() < 12):
            self.pan_table_output.setRowCount(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.pan_table_output.setVerticalHeaderItem(11, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.pan_table_output.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.pan_table_output.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.pan_table_output.setItem(2, 0, __qtablewidgetitem15)
        self.pan_table_output.setObjectName(u"pan_table_output")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pan_table_output.sizePolicy().hasHeightForWidth())
        self.pan_table_output.setSizePolicy(sizePolicy)
        font11 = QFont()
        font11.setPointSize(12)
        self.pan_table_output.setFont(font11)
        self.pan_table_output.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(47, 47, 47);\n"
"	alternate-background-color: rgb(40, 40, 40);\n"
"	font-size: 12pt;\n"
"	border: 1px solid #fffff8;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color: #646464;\n"
"    border-style: none;\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 5px;\n"
"    font-size: 10pt;\n"
"    border-style: none;\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.pan_table_output.setAlternatingRowColors(True)
        self.pan_table_output.setShowGrid(True)
        self.pan_table_output.setGridStyle(Qt.DashDotLine)
        self.pan_table_output.setSortingEnabled(False)
        self.pan_table_output.setCornerButtonEnabled(True)
        self.pan_table_output.setColumnCount(1)
        self.pan_table_output.horizontalHeader().setVisible(False)
        self.pan_table_output.horizontalHeader().setCascadingSectionResizes(False)
        self.pan_table_output.horizontalHeader().setMinimumSectionSize(50)
        self.pan_table_output.horizontalHeader().setDefaultSectionSize(100)
        self.pan_table_output.horizontalHeader().setStretchLastSection(True)
        self.pan_table_output.verticalHeader().setVisible(True)
        self.pan_table_output.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.pan_table_output)

        self.pan_output.addTab(self.pan_table_output_page, "")
        self.raw_pan_out_page = QWidget()
        self.raw_pan_out_page.setObjectName(u"raw_pan_out_page")
        self.verticalLayout_29 = QVBoxLayout(self.raw_pan_out_page)
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.raw_output_container = QScrollArea(self.raw_pan_out_page)
        self.raw_output_container.setObjectName(u"raw_output_container")
        self.raw_output_container.setWidgetResizable(True)
        self.raw_output_container_scrol = QWidget()
        self.raw_output_container_scrol.setObjectName(u"raw_output_container_scrol")
        self.raw_output_container_scrol.setGeometry(QRect(0, 0, 616, 420))
        self.verticalLayout_28 = QVBoxLayout(self.raw_output_container_scrol)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.raw_pan_output = QLabel(self.raw_output_container_scrol)
        self.raw_pan_output.setObjectName(u"raw_pan_output")
        self.raw_pan_output.setFont(font11)

        self.verticalLayout_28.addWidget(self.raw_pan_output, 0, Qt.AlignTop)

        self.raw_output_container.setWidget(self.raw_output_container_scrol)

        self.verticalLayout_29.addWidget(self.raw_output_container)

        self.pan_output.addTab(self.raw_pan_out_page, "")

        self.verticalLayout_20.addWidget(self.pan_output)

        self.main_content_pages.addWidget(self.tax_pan_search)

        self.horizontalLayout_7.addWidget(self.main_content_pages)


        self.gridLayout.addWidget(self.content_frame, 1, 2, 2, 1)

        self.left_menu_frame = QFrame(self.contents)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setStyleSheet(u"padding: 0px;")
        self.left_menu_frame.setFrameShape(QFrame.NoFrame)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.dashboard_menu = QPushButton(self.left_menu_frame)
        self.dashboard_menu.setObjectName(u"dashboard_menu")
        self.dashboard_menu.setEnabled(True)
        font12 = QFont()
        font12.setFamilies([u"Helvetica"])
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setUnderline(False)
        font12.setStrikeOut(False)
        self.dashboard_menu.setFont(font12)
        self.dashboard_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_menu.setMouseTracking(False)
        self.dashboard_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_menu.setIcon(icon14)
        self.dashboard_menu.setIconSize(QSize(16, 16))
        self.dashboard_menu.setCheckable(True)
        self.dashboard_menu.setChecked(True)
        self.dashboard_menu.setAutoRepeat(False)
        self.dashboard_menu.setAutoDefault(True)
        self.dashboard_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.dashboard_menu)

        self.utilities_menu = QPushButton(self.left_menu_frame)
        self.utilities_menu.setObjectName(u"utilities_menu")
        self.utilities_menu.setFont(font12)
        self.utilities_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.utilities_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.utilities_menu.setIcon(icon15)
        self.utilities_menu.setIconSize(QSize(16, 16))
        self.utilities_menu.setCheckable(True)
        self.utilities_menu.setAutoRepeat(False)
        self.utilities_menu.setAutoDefault(False)
        self.utilities_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.utilities_menu)

        self.api_menu = QPushButton(self.left_menu_frame)
        self.api_menu.setObjectName(u"api_menu")
        self.api_menu.setFont(font12)
        self.api_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.api_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.api_menu.setIcon(icon16)
        self.api_menu.setIconSize(QSize(16, 16))
        self.api_menu.setCheckable(True)
        self.api_menu.setAutoRepeat(False)
        self.api_menu.setAutoDefault(False)
        self.api_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.api_menu)

        self.tax_menu = QPushButton(self.left_menu_frame)
        self.tax_menu.setObjectName(u"tax_menu")
        self.tax_menu.setFont(font12)
        self.tax_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.tax_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tax_menu.setIcon(icon17)
        self.tax_menu.setIconSize(QSize(16, 16))
        self.tax_menu.setCheckable(True)
        self.tax_menu.setAutoRepeat(False)
        self.tax_menu.setAutoDefault(False)
        self.tax_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.tax_menu)

        self.lms_menu = QPushButton(self.left_menu_frame)
        self.lms_menu.setObjectName(u"lms_menu")
        self.lms_menu.setFont(font12)
        self.lms_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.lms_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(223, 223, 221, 150);\n"
"	color: rgb(0,0,0);\n"
"	padding: 10px;\n"
"	margin: 5px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(223, 223, 221, 200);\n"
"	border-right: rgba(85, 0, 255, 150) 4px solid;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lms_menu.setIcon(icon18)
        self.lms_menu.setIconSize(QSize(16, 16))
        self.lms_menu.setCheckable(True)
        self.lms_menu.setAutoRepeat(False)
        self.lms_menu.setAutoDefault(False)
        self.lms_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.lms_menu)


        self.gridLayout.addWidget(self.left_menu_frame, 1, 0, 1, 1, Qt.AlignTop)

        self.sub_menu_frame = QFrame(self.contents)
        self.sub_menu_frame.setObjectName(u"sub_menu_frame")
        self.sub_menu_frame.setMinimumSize(QSize(0, 0))
        self.sub_menu_frame.setMaximumSize(QSize(175, 16777215))
        self.sub_menu_frame.setStyleSheet(u"background-color: rgb(37, 37, 38);\n"
"padding: 2px;\n"
"border-radius: 0px;")
        self.sub_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.sub_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.sub_menu_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.submenu_pages = QStackedWidget(self.sub_menu_frame)
        self.submenu_pages.setObjectName(u"submenu_pages")
        self.submenu_pages.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(50, 50, 50, 200);\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	font-size: 10pt;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(29, 29, 29);\n"
"	border-radius: 4px;\n"
"}")
        self.dashboard_menus = QWidget()
        self.dashboard_menus.setObjectName(u"dashboard_menus")
        self.verticalLayout_7 = QVBoxLayout(self.dashboard_menus)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.home_page = QPushButton(self.dashboard_menus)
        self.home_page.setObjectName(u"home_page")
        font13 = QFont()
        font13.setPointSize(10)
        font13.setBold(True)
        self.home_page.setFont(font13)
        self.home_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.home_page)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.submenu_pages.addWidget(self.dashboard_menus)
        self.utilites_menus = QWidget()
        self.utilites_menus.setObjectName(u"utilites_menus")
        self.verticalLayout_13 = QVBoxLayout(self.utilites_menus)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.numbers_page = QPushButton(self.utilites_menus)
        self.numbers_page.setObjectName(u"numbers_page")
        font14 = QFont()
        font14.setPointSize(10)
        font14.setBold(True)
        font14.setItalic(False)
        font14.setKerning(True)
        self.numbers_page.setFont(font14)
        self.numbers_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.numbers_page.setStyleSheet(u"")
        self.numbers_page.setIcon(icon17)
        self.numbers_page.setIconSize(QSize(16, 16))

        self.verticalLayout_13.addWidget(self.numbers_page)

        self.join_pdf_page = QPushButton(self.utilites_menus)
        self.join_pdf_page.setObjectName(u"join_pdf_page")
        self.join_pdf_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.join_pdf_page)

        self.image_extraction_page = QPushButton(self.utilites_menus)
        self.image_extraction_page.setObjectName(u"image_extraction_page")
        self.image_extraction_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.image_extraction_page)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.submenu_pages.addWidget(self.utilites_menus)
        self.apis_menus = QWidget()
        self.apis_menus.setObjectName(u"apis_menus")
        self.verticalLayout_14 = QVBoxLayout(self.apis_menus)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton = QPushButton(self.apis_menus)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.submenu_pages.addWidget(self.apis_menus)
        self.tax_menus = QWidget()
        self.tax_menus.setObjectName(u"tax_menus")
        self.verticalLayout_15 = QVBoxLayout(self.tax_menus)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pan_search_page_btn = QPushButton(self.tax_menus)
        self.pan_search_page_btn.setObjectName(u"pan_search_page_btn")
        self.pan_search_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pan_search_page_btn.setIcon(icon13)

        self.verticalLayout_15.addWidget(self.pan_search_page_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.submenu_pages.addWidget(self.tax_menus)
        self.lms_menus = QWidget()
        self.lms_menus.setObjectName(u"lms_menus")
        self.verticalLayout_16 = QVBoxLayout(self.lms_menus)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_3 = QPushButton(self.lms_menus)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_5)

        self.submenu_pages.addWidget(self.lms_menus)
        self.settings_menus = QWidget()
        self.settings_menus.setObjectName(u"settings_menus")
        self.verticalLayout_17 = QVBoxLayout(self.settings_menus)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_4 = QPushButton(self.settings_menus)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.pushButton_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_6)

        self.submenu_pages.addWidget(self.settings_menus)
        self.help_menus = QWidget()
        self.help_menus.setObjectName(u"help_menus")
        self.verticalLayout_18 = QVBoxLayout(self.help_menus)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_5 = QPushButton(self.help_menus)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_18.addWidget(self.pushButton_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_7)

        self.submenu_pages.addWidget(self.help_menus)
        self.about_menus = QWidget()
        self.about_menus.setObjectName(u"about_menus")
        self.verticalLayout_19 = QVBoxLayout(self.about_menus)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.about_app = QPushButton(self.about_menus)
        self.about_app.setObjectName(u"about_app")
        self.about_app.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_19.addWidget(self.about_app)

        self.about_developer = QPushButton(self.about_menus)
        self.about_developer.setObjectName(u"about_developer")
        self.about_developer.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_19.addWidget(self.about_developer)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)

        self.submenu_pages.addWidget(self.about_menus)

        self.verticalLayout_6.addWidget(self.submenu_pages)


        self.gridLayout.addWidget(self.sub_menu_frame, 1, 1, 2, 1)

        self.brand_frame = QFrame(self.contents)
        self.brand_frame.setObjectName(u"brand_frame")
        self.brand_frame.setMinimumSize(QSize(25, 75))
        self.brand_frame.setMaximumSize(QSize(75, 75))
        self.brand_frame.setFrameShape(QFrame.StyledPanel)
        self.brand_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.brand_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.brand_logo = QLabel(self.brand_frame)
        self.brand_logo.setObjectName(u"brand_logo")
        self.brand_logo.setPixmap(QPixmap(u"../../../../.designer/icon.ico"))
        self.brand_logo.setScaledContents(True)
        self.brand_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.brand_logo)


        self.gridLayout.addWidget(self.brand_frame, 0, 0, 1, 1)

        self.right_menu_container = QFrame(self.contents)
        self.right_menu_container.setObjectName(u"right_menu_container")
        self.right_menu_container.setMinimumSize(QSize(175, 0))
        self.right_menu_container.setMaximumSize(QSize(175, 16777215))
        self.right_menu_container.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(37, 37, 38);\n"
"	padding: 2px;\n"
"	border-bottom-left-radius: 2px;\n"
"	border-bottom-right-radius: 2px;\n"
"	border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QLabel{\n"
"	height: 50;\n"
"	font-size: 10;\n"
"	font-weight: bold;\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	height: 25;\n"
"	font-size: 10;\n"
"	background-color: rgb(47, 47, 47);\n"
"	padding: 5;\n"
"	border-bottom: 2px solid grey;\n"
"}\n"
"\n"
"QWidget{\n"
"	padding: 5;\n"
"}")
        self.right_menu_container.setFrameShape(QFrame.StyledPanel)
        self.right_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.right_menu_container)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.right_menu_container)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(37, 37, 38);")
        self.scrollArea.setWidgetResizable(True)
        self.right_menu = QWidget()
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setGeometry(QRect(0, 0, 155, 600))
        self.verticalLayout_21 = QVBoxLayout(self.right_menu)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.right_menu)

        self.verticalLayout_12.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.right_menu_container, 0, 3, 3, 1)


        self.verticalLayout.addWidget(self.contents)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 30))
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(0, 122, 204);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.credit_frame = QFrame(self.credits_bar)
        self.credit_frame.setObjectName(u"credit_frame")
        self.credit_frame.setFrameShape(QFrame.NoFrame)
        self.credit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.credit_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, 0, 0, 0)
        self.status_label = QLabel(self.credit_frame)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_4.addWidget(self.status_label)

        self.credit_label = QLabel(self.credit_frame)
        self.credit_label.setObjectName(u"credit_label")
        self.credit_label.setMinimumSize(QSize(510, 0))
        self.credit_label.setMaximumSize(QSize(510, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Times New Roman"])
        font15.setPointSize(10)
        font15.setBold(True)
        font15.setItalic(True)
        self.credit_label.setFont(font15)
        self.credit_label.setStyleSheet(u"")
        self.credit_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.credit_label)


        self.horizontalLayout_3.addWidget(self.credit_frame)

        self.grip_frame = QFrame(self.credits_bar)
        self.grip_frame.setObjectName(u"grip_frame")
        self.grip_frame.setMinimumSize(QSize(30, 30))
        self.grip_frame.setMaximumSize(QSize(30, 30))
        self.grip_frame.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.grip_frame.setStyleSheet(u"padding: 5px;")
        self.grip_frame.setFrameShape(QFrame.StyledPanel)
        self.grip_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.grip_frame)


        self.verticalLayout.addWidget(self.credits_bar)


        self.verticalLayout_26.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_content_pages.setCurrentIndex(4)
        self.pan_output.setCurrentIndex(0)
        self.dashboard_menu.setDefault(True)
        self.utilities_menu.setDefault(False)
        self.api_menu.setDefault(False)
        self.tax_menu.setDefault(False)
        self.lms_menu.setDefault(False)
        self.submenu_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Maya Utility App v1.0.0", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"Maya Utility App v1.0.0", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_minimize.setStatusTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(statustip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_maximize.setStatusTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(statustip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_close.setStatusTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(statustip)
        self.btn_close.setText("")
        self.settings_menu.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.help_menu.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about_menu.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Good Morning! Ajay Singh", None))
        self.quotes_label.setText(QCoreApplication.translate("MainWindow", u"Turn your wounds into wisdom", None))
        self.nepali_date.setText(QCoreApplication.translate("MainWindow", u"2079-03-22", None))
        self.intdt_copy_btn.setText("")
        self.int_date.setText(QCoreApplication.translate("MainWindow", u"2022-07-06", None))
        self.npdt_copy_btn.setText("")
        self.np_cal_btn.setText(QCoreApplication.translate("MainWindow", u"NP", None))
        self.options_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"I am a Dashboard UI", None))
        self.number_input_label.setText(QCoreApplication.translate("MainWindow", u"Enter your number:", None))
        self.num_input.setInputMask("")
        self.num_input.setText("")
        self.clear_btn.setText("")
        self.copy_num_all_btn.setText("")
        self.convert_btn.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.decimal_lbl.setText(QCoreApplication.translate("MainWindow", u"Decimal:", None))
        self.eng_lbl.setText(QCoreApplication.translate("MainWindow", u"English:", None))
        self.nep_words_copy_btn.setText("")
        self.whole_lbl.setText(QCoreApplication.translate("MainWindow", u"Whole:", None))
        self.lakh_copy_btn.setText("")
        self.num_copy_btn.setText("")
        self.words_nep_disp.setText("")
        self.words_nep_lbl.setText(QCoreApplication.translate("MainWindow", u"Words Lakh Nep:", None))
        self.nep_copy_btn.setText("")
        self.lakh_lbl.setText(QCoreApplication.translate("MainWindow", u"Lakh Format:", None))
        self.nepali_lbl.setText(QCoreApplication.translate("MainWindow", u"Nepali:", None))
        self.num_lbl.setText(QCoreApplication.translate("MainWindow", u"Number:", None))
        self.eng_words_copy_btn.setText("")
        self.words_eng_lbl.setText(QCoreApplication.translate("MainWindow", u"Words Million Eng:", None))
        self.million_lbl.setText(QCoreApplication.translate("MainWindow", u"Million Format:", None))
        self.whole_copy_btn.setText("")
        self.words_eng_disp.setText("")
        self.eng_copy_btn.setText("")
        self.million_copy_btn.setText("")
        self.decimal_copy_btn.setText("")
        self.add_pdf_files_btn.setText(QCoreApplication.translate("MainWindow", u"Add Files", None))
        self.remove_pdf_file_btn.setText(QCoreApplication.translate("MainWindow", u"Remove File", None))
        self.clear_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Files", None))
        self.pdf_move_up_btn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.pdf_move_down_btn.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.save_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.select_file_btn.setText(QCoreApplication.translate("MainWindow", u"Either Drop or Select File", None))
        self.Image_Label.setText(QCoreApplication.translate("MainWindow", u"Image will be Shown Here...", None))
        self.extracted_texts.setMarkdown("")
        self.extracted_texts.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.extracted_texts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your result will be shown Here  ", None))
        self.pan_input_label.setText(QCoreApplication.translate("MainWindow", u"Enter your number:", None))
        self.pan_input.setText("")
#if QT_CONFIG(tooltip)
        self.clear_pan_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the Input", None))
#endif // QT_CONFIG(tooltip)
        self.clear_pan_btn.setText("")
#if QT_CONFIG(tooltip)
        self.copy_pan_raw_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Copy Raw Data", None))
#endif // QT_CONFIG(tooltip)
        self.copy_pan_raw_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pan_search_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Search the VAT/PAN Number", None))
#endif // QT_CONFIG(tooltip)
        self.pan_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.pan_table_output.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem1 = self.pan_table_output.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name in English", None));
        ___qtablewidgetitem2 = self.pan_table_output.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name in Nepali", None));
        ___qtablewidgetitem3 = self.pan_table_output.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"VAT/PAN No", None));
        ___qtablewidgetitem4 = self.pan_table_output.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem5 = self.pan_table_output.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Mobile", None));
        ___qtablewidgetitem6 = self.pan_table_output.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem7 = self.pan_table_output.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Eff. Reg. Date", None));
        ___qtablewidgetitem8 = self.pan_table_output.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Registered Office", None));
        ___qtablewidgetitem9 = self.pan_table_output.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Personal PAN", None));
        ___qtablewidgetitem10 = self.pan_table_output.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Tax Clearance", None));
        ___qtablewidgetitem11 = self.pan_table_output.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Account Status", None));
        ___qtablewidgetitem12 = self.pan_table_output.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Businesses", None));

        __sortingEnabled = self.pan_table_output.isSortingEnabled()
        self.pan_table_output.setSortingEnabled(False)
        self.pan_table_output.setSortingEnabled(__sortingEnabled)

        self.pan_output.setTabText(self.pan_output.indexOf(self.pan_table_output_page), QCoreApplication.translate("MainWindow", u"PAN/VAT Details", None))
        self.raw_pan_output.setText(QCoreApplication.translate("MainWindow", u"Details will be shown Here!", None))
        self.pan_output.setTabText(self.pan_output.indexOf(self.raw_pan_out_page), QCoreApplication.translate("MainWindow", u"RAW Data", None))
        self.dashboard_menu.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(shortcut)
        self.dashboard_menu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.utilities_menu.setText(QCoreApplication.translate("MainWindow", u"Uitlites", None))
#if QT_CONFIG(shortcut)
        self.utilities_menu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.api_menu.setText(QCoreApplication.translate("MainWindow", u"API", None))
#if QT_CONFIG(shortcut)
        self.api_menu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.tax_menu.setText(QCoreApplication.translate("MainWindow", u"TAX", None))
#if QT_CONFIG(shortcut)
        self.tax_menu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.lms_menu.setText(QCoreApplication.translate("MainWindow", u"Library", None))
#if QT_CONFIG(shortcut)
        self.lms_menu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.home_page.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.numbers_page.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.join_pdf_page.setText(QCoreApplication.translate("MainWindow", u"PDF Join", None))
        self.image_extraction_page.setText(QCoreApplication.translate("MainWindow", u"Text Extraction", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"APiS", None))
        self.pan_search_page_btn.setText(QCoreApplication.translate("MainWindow", u" Pan Search", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about_app.setText(QCoreApplication.translate("MainWindow", u"About App", None))
        self.about_developer.setText(QCoreApplication.translate("MainWindow", u"About Developer", None))
        self.brand_logo.setText("")
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.credit_label.setText(QCoreApplication.translate("MainWindow", u"Copyright @ Ajay Singh [Maya] 2022. All the rights are reserved.", None))
    # retranslateUi

