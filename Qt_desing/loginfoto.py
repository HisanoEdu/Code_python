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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)
import Imagens.qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1235, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 30, 141, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 190, 101, 41))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 260, 231, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(81, 82, 85);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 330, 231, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(81, 82, 85);")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(200, 440, 141, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 570, 49, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 450, 49, 16))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 270, 49, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 340, 49, 16))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 370, 121, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 10, 941, 531))
        self.label_9.setPixmap(QPixmap(u":/icon/wandinha.webp"))
        self.label_9.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1235, 22))
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Esqueceu senha", None))
        self.label_9.setText("")
        self.menuLogin_icon.setTitle(QCoreApplication.translate("MainWindow", u"Login icon", None))
    # retranslateUi

import loginfoto, sys
from loginfoto import Ui_MainWindow
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
    


