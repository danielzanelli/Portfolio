# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(800, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(800, 160))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 80))
        self.scrollArea.setMaximumSize(QSize(16777215, 160))
        font = QFont()
        font.setPointSize(20)
        self.scrollArea.setFont(font)
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 496, 97))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setFocusPolicy(Qt.WheelFocus)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_17 = QPushButton(self.frame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMaximumSize(QSize(120, 100))
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton_17.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.pushButton_21 = QPushButton(self.frame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setMaximumSize(QSize(120, 16777215))
        self.pushButton_21.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_21)

        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMaximumSize(QSize(120, 100))
        self.pushButton_13.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMaximumSize(QSize(120, 100))
        self.pushButton_14.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_14)

        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMaximumSize(QSize(120, 16777215))
        self.pushButton_19.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_19)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 4, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(100, 100))
        font2 = QFont()
        font2.setPointSize(14)
        self.pushButton_4.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_4, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(100, 100))
        self.pushButton_7.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QSize(100, 100))
        self.pushButton_9.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMaximumSize(QSize(100, 100))
        self.pushButton_10.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(100, 100))
        self.pushButton_6.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QSize(100, 100))
        self.pushButton_8.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(100, 100))
        self.pushButton_3.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(100, 100))
        self.pushButton_5.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(100, 100))
        self.pushButton_2.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMaximumSize(QSize(16777215, 100))
        self.pushButton_18.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_18, 4, 0, 1, 3)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QSize(16777215, 100))
        self.pushButton_11.setFont(font1)

        self.gridLayout_5.addWidget(self.pushButton_11, 3, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 4, 4, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 4, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMaximumSize(QSize(120, 100))
        self.pushButton_16.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_16)

        self.pushButton_22 = QPushButton(self.frame)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setMaximumSize(QSize(120, 16777215))
        self.pushButton_22.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_22)

        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMaximumSize(QSize(120, 100))
        self.pushButton_12.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMaximumSize(QSize(120, 100))
        self.pushButton_15.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_15)

        self.pushButton_20 = QPushButton(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMaximumSize(QSize(120, 16777215))
        self.pushButton_20.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_20)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 4, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_24 = QPushButton(self.frame)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setMaximumSize(QSize(120, 16777215))
        self.pushButton_24.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_24)

        self.pushButton_23 = QPushButton(self.frame)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMaximumSize(QSize(120, 16777215))
        self.pushButton_23.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_23)

        self.pushButton_25 = QPushButton(self.frame)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setMaximumSize(QSize(120, 16777215))
        self.pushButton_25.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.frame)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setMaximumSize(QSize(120, 16777215))
        self.pushButton_26.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setMaximumSize(QSize(120, 16777215))
        self.pushButton_27.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_27)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 4, 1)


        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 39))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
    # retranslateUi

