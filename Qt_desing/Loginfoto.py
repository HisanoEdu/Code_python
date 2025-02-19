# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Loginfoto.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1204, 617)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(180, 20, 931, 521))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 141, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 290, 49, 16))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 220, 231, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(81, 82, 85);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 230, 49, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 280, 231, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(81, 82, 85);")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 380, 181, 31))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 160, 131, 41))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"font: 22pt \"Segoe UI\";")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 931, 541))
        self.label.setPixmap(QPixmap(u":/icon/Avengers.jpg"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.label_6.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1204, 22))
        self.menuLogin_icon = QMenu(self.menubar)
        self.menuLogin_icon.setObjectName(u"menuLogin_icon")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLogin_icon.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CineFilmes", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText("")
        self.menuLogin_icon.setTitle(QCoreApplication.translate("MainWindow", u"Login icon", None))
    # retranslateUi

