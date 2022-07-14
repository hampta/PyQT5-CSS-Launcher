# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication,
    QMetaObject, QRect, QSize, Qt)
from PySide2.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 311)
        MainWindow.setMinimumSize(QSize(750, 311))
        MainWindow.setMaximumSize(QSize(750, 311))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(750, 311))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 190, 731, 112))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.checkinfoL = QLabel(self.layoutWidget)
        self.checkinfoL.setObjectName(u"checkinfoL")
        self.checkinfoL.setEnabled(False)
        self.checkinfoL.setMouseTracking(False)
        self.checkinfoL.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.checkinfoL)

        self.filecheckL = QLabel(self.layoutWidget)
        self.filecheckL.setObjectName(u"filecheckL")
        self.filecheckL.setEnabled(False)

        self.verticalLayout_2.addWidget(self.filecheckL)

        self.onefileBar = QProgressBar(self.layoutWidget)
        self.onefileBar.setObjectName(u"onefileBar")
        self.onefileBar.setMinimumSize(QSize(617, 25))
        self.onefileBar.setMaximumSize(QSize(617, 25))
        self.onefileBar.setValue(0)
        self.onefileBar.setAlignment(Qt.AlignCenter)
        self.onefileBar.setOrientation(Qt.Horizontal)
        self.onefileBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.onefileBar)

        self.allfilesBar = QProgressBar(self.layoutWidget)
        self.allfilesBar.setObjectName(u"allfilesBar")
        self.allfilesBar.setMinimumSize(QSize(617, 25))
        self.allfilesBar.setMaximumSize(QSize(617, 25))
        self.allfilesBar.setValue(0)
        self.allfilesBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.allfilesBar)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.othertoolButton = QToolButton(self.layoutWidget)
        self.othertoolButton.setObjectName(u"othertoolButton")
        self.othertoolButton.setMinimumSize(QSize(35, 35))
        self.othertoolButton.setMaximumSize(QSize(22, 22))

        self.verticalLayout.addWidget(self.othertoolButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.downloadButton = QPushButton(self.layoutWidget)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setMinimumSize(QSize(90, 50))
        self.downloadButton.setMaximumSize(QSize(90, 50))

        self.verticalLayout.addWidget(self.downloadButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 161, 166))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.nicknameL = QLabel(self.layoutWidget1)
        self.nicknameL.setObjectName(u"nicknameL")

        self.verticalLayout_3.addWidget(self.nicknameL)

        self.nicknameEdit = QLineEdit(self.layoutWidget1)
        self.nicknameEdit.setObjectName(u"nicknameEdit")

        self.verticalLayout_3.addWidget(self.nicknameEdit)

        self.clanL = QLabel(self.layoutWidget1)
        self.clanL.setObjectName(u"clanL")

        self.verticalLayout_3.addWidget(self.clanL)

        self.clanEdit = QLineEdit(self.layoutWidget1)
        self.clanEdit.setObjectName(u"clanEdit")

        self.verticalLayout_3.addWidget(self.clanEdit)

        self.playButton = QPushButton(self.layoutWidget1)
        self.playButton.setObjectName(u"playButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QSize(155, 60))
        self.playButton.setMaximumSize(QSize(155, 60))
        self.playButton.setAutoFillBackground(False)
        self.playButton.setCheckable(False)
        self.playButton.setAutoDefault(False)
        self.playButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.playButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.playButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkinfoL.setText("")
        self.filecheckL.setText("")
        self.othertoolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.nicknameL.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a\u043d\u0435\u0439\u043c", None))
        self.clanL.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u043d-\u0442\u0435\u0433", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
    # retranslateUi

