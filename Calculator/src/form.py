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
        MainWindow.resize(644, 800)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 540, 97))
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
        self.clearButton = QPushButton(self.frame)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMaximumSize(QSize(120, 100))
        font1 = QFont()
        font1.setPointSize(16)
        self.clearButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.clearButton)

        self.powerButton = QPushButton(self.frame)
        self.powerButton.setObjectName(u"powerButton")
        sizePolicy.setHeightForWidth(self.powerButton.sizePolicy().hasHeightForWidth())
        self.powerButton.setSizePolicy(sizePolicy)
        self.powerButton.setMaximumSize(QSize(120, 16777215))
        self.powerButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.powerButton)

        self.divideButton = QPushButton(self.frame)
        self.divideButton.setObjectName(u"divideButton")
        sizePolicy.setHeightForWidth(self.divideButton.sizePolicy().hasHeightForWidth())
        self.divideButton.setSizePolicy(sizePolicy)
        self.divideButton.setMaximumSize(QSize(120, 100))
        self.divideButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.divideButton)

        self.multiplyButton = QPushButton(self.frame)
        self.multiplyButton.setObjectName(u"multiplyButton")
        sizePolicy.setHeightForWidth(self.multiplyButton.sizePolicy().hasHeightForWidth())
        self.multiplyButton.setSizePolicy(sizePolicy)
        self.multiplyButton.setMaximumSize(QSize(120, 100))
        self.multiplyButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.multiplyButton)

        self.openParenthesisButton = QPushButton(self.frame)
        self.openParenthesisButton.setObjectName(u"openParenthesisButton")
        sizePolicy.setHeightForWidth(self.openParenthesisButton.sizePolicy().hasHeightForWidth())
        self.openParenthesisButton.setSizePolicy(sizePolicy)
        self.openParenthesisButton.setMaximumSize(QSize(120, 16777215))
        self.openParenthesisButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.openParenthesisButton)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 4, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.threeButton = QPushButton(self.frame)
        self.threeButton.setObjectName(u"threeButton")
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        self.threeButton.setMaximumSize(QSize(100, 100))
        font2 = QFont()
        font2.setPointSize(14)
        self.threeButton.setFont(font2)

        self.gridLayout_5.addWidget(self.threeButton, 2, 2, 1, 1)

        self.zeroButton = QPushButton(self.frame)
        self.zeroButton.setObjectName(u"zeroButton")
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setMaximumSize(QSize(100, 100))
        self.zeroButton.setFont(font2)

        self.gridLayout_5.addWidget(self.zeroButton, 3, 0, 1, 1)

        self.sixButton = QPushButton(self.frame)
        self.sixButton.setObjectName(u"sixButton")
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        self.sixButton.setMaximumSize(QSize(100, 100))
        self.sixButton.setFont(font2)

        self.gridLayout_5.addWidget(self.sixButton, 1, 2, 1, 1)

        self.eightButton = QPushButton(self.frame)
        self.eightButton.setObjectName(u"eightButton")
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        self.eightButton.setMaximumSize(QSize(100, 100))
        self.eightButton.setFont(font2)

        self.gridLayout_5.addWidget(self.eightButton, 0, 1, 1, 1)

        self.nineButton = QPushButton(self.frame)
        self.nineButton.setObjectName(u"nineButton")
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        self.nineButton.setMaximumSize(QSize(100, 100))
        self.nineButton.setFont(font2)

        self.gridLayout_5.addWidget(self.nineButton, 0, 2, 1, 1)

        self.fiveButton = QPushButton(self.frame)
        self.fiveButton.setObjectName(u"fiveButton")
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        self.fiveButton.setMaximumSize(QSize(100, 100))
        self.fiveButton.setFont(font2)

        self.gridLayout_5.addWidget(self.fiveButton, 1, 1, 1, 1)

        self.sevenButton = QPushButton(self.frame)
        self.sevenButton.setObjectName(u"sevenButton")
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        self.sevenButton.setMaximumSize(QSize(100, 100))
        self.sevenButton.setFont(font2)

        self.gridLayout_5.addWidget(self.sevenButton, 0, 0, 1, 1)

        self.twoButton = QPushButton(self.frame)
        self.twoButton.setObjectName(u"twoButton")
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        self.twoButton.setMaximumSize(QSize(100, 100))
        self.twoButton.setFont(font2)

        self.gridLayout_5.addWidget(self.twoButton, 2, 1, 1, 1)

        self.fourButton = QPushButton(self.frame)
        self.fourButton.setObjectName(u"fourButton")
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        self.fourButton.setMaximumSize(QSize(100, 100))
        self.fourButton.setFont(font2)

        self.gridLayout_5.addWidget(self.fourButton, 1, 0, 1, 1)

        self.oneButton = QPushButton(self.frame)
        self.oneButton.setObjectName(u"oneButton")
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        self.oneButton.setMaximumSize(QSize(100, 100))
        self.oneButton.setFont(font2)

        self.gridLayout_5.addWidget(self.oneButton, 2, 0, 1, 1)

        self.equalsButton = QPushButton(self.frame)
        self.equalsButton.setObjectName(u"equalsButton")
        self.equalsButton.setMaximumSize(QSize(16777215, 100))
        self.equalsButton.setFont(font)

        self.gridLayout_5.addWidget(self.equalsButton, 4, 0, 1, 3)

        self.decimalButton = QPushButton(self.frame)
        self.decimalButton.setObjectName(u"decimalButton")
        sizePolicy.setHeightForWidth(self.decimalButton.sizePolicy().hasHeightForWidth())
        self.decimalButton.setSizePolicy(sizePolicy)
        self.decimalButton.setMaximumSize(QSize(16777215, 100))
        self.decimalButton.setFont(font1)

        self.gridLayout_5.addWidget(self.decimalButton, 3, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 4, 4, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 4, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMaximumSize(QSize(120, 100))
        self.deleteButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.deleteButton)

        self.squareRootButton = QPushButton(self.frame)
        self.squareRootButton.setObjectName(u"squareRootButton")
        sizePolicy.setHeightForWidth(self.squareRootButton.sizePolicy().hasHeightForWidth())
        self.squareRootButton.setSizePolicy(sizePolicy)
        self.squareRootButton.setMaximumSize(QSize(120, 16777215))
        self.squareRootButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.squareRootButton)

        self.negativeButton = QPushButton(self.frame)
        self.negativeButton.setObjectName(u"negativeButton")
        sizePolicy.setHeightForWidth(self.negativeButton.sizePolicy().hasHeightForWidth())
        self.negativeButton.setSizePolicy(sizePolicy)
        self.negativeButton.setMaximumSize(QSize(120, 100))
        self.negativeButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.negativeButton)

        self.addButton = QPushButton(self.frame)
        self.addButton.setObjectName(u"addButton")
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMaximumSize(QSize(120, 100))
        self.addButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.addButton)

        self.closeParenthesisButton = QPushButton(self.frame)
        self.closeParenthesisButton.setObjectName(u"closeParenthesisButton")
        sizePolicy.setHeightForWidth(self.closeParenthesisButton.sizePolicy().hasHeightForWidth())
        self.closeParenthesisButton.setSizePolicy(sizePolicy)
        self.closeParenthesisButton.setMaximumSize(QSize(120, 16777215))
        self.closeParenthesisButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.closeParenthesisButton)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 4, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cosButton = QPushButton(self.frame)
        self.cosButton.setObjectName(u"cosButton")
        sizePolicy.setHeightForWidth(self.cosButton.sizePolicy().hasHeightForWidth())
        self.cosButton.setSizePolicy(sizePolicy)
        self.cosButton.setMaximumSize(QSize(120, 16777215))
        self.cosButton.setFont(font1)

        self.verticalLayout_4.addWidget(self.cosButton)

        self.sinButton = QPushButton(self.frame)
        self.sinButton.setObjectName(u"sinButton")
        sizePolicy.setHeightForWidth(self.sinButton.sizePolicy().hasHeightForWidth())
        self.sinButton.setSizePolicy(sizePolicy)
        self.sinButton.setMaximumSize(QSize(120, 16777215))
        self.sinButton.setFont(font1)

        self.verticalLayout_4.addWidget(self.sinButton)

        self.tanButton = QPushButton(self.frame)
        self.tanButton.setObjectName(u"tanButton")
        sizePolicy.setHeightForWidth(self.tanButton.sizePolicy().hasHeightForWidth())
        self.tanButton.setSizePolicy(sizePolicy)
        self.tanButton.setMaximumSize(QSize(120, 16777215))
        self.tanButton.setFont(font1)

        self.verticalLayout_4.addWidget(self.tanButton)

        self.logButton = QPushButton(self.frame)
        self.logButton.setObjectName(u"logButton")
        sizePolicy.setHeightForWidth(self.logButton.sizePolicy().hasHeightForWidth())
        self.logButton.setSizePolicy(sizePolicy)
        self.logButton.setMaximumSize(QSize(120, 16777215))
        self.logButton.setFont(font1)

        self.verticalLayout_4.addWidget(self.logButton)

        self.piButton = QPushButton(self.frame)
        self.piButton.setObjectName(u"piButton")
        sizePolicy.setHeightForWidth(self.piButton.sizePolicy().hasHeightForWidth())
        self.piButton.setSizePolicy(sizePolicy)
        self.piButton.setMaximumSize(QSize(120, 16777215))
        self.piButton.setFont(font1)

        self.verticalLayout_4.addWidget(self.piButton)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 4, 1)


        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 644, 39))
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
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.powerButton.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.divideButton.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.multiplyButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.openParenthesisButton.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.threeButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.zeroButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.sixButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.eightButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nineButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.fiveButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.sevenButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.twoButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.fourButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.oneButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.equalsButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.decimalButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.squareRootButton.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.negativeButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.closeParenthesisButton.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.cosButton.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.sinButton.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.tanButton.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.logButton.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.piButton.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
    # retranslateUi

