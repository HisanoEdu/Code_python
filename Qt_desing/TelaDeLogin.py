# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela de login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(745, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Senha = QListView(self.centralwidget)
        self.Senha.setObjectName(u"Senha")
        self.Senha.setGeometry(QRect(240, 90, 371, 381))
        font = QFont()
        font.setPointSize(10)
        self.Senha.setFont(font)
        self.Senha.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 100, 101, 41))
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 160, 49, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 250, 49, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 180, 241, 31))
        self.lineEdit.setStyleSheet(u"alternate-background-color: rgb(255, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(300, 270, 241, 31))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(360, 360, 113, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 360, 49, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 310, 101, 16))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 400, 71, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 745, 22))
        self.menuLogin = QMenu(self.menubar)
        self.menuLogin.setObjectName(u"menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Recuperar senha", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Registrar-se", None))
        self.menuLogin.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi


import TelaDeLogin, sys
from TelaDeLogin import Ui_MainWindow
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())