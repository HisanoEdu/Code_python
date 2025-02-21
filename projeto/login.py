
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import fotos

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(921, 624)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.telaLogin = QFrame(self.centralwidget)
        self.telaLogin.setObjectName(u"telaLogin")
        self.telaLogin.setGeometry(QRect(60, 50, 821, 511))
        self.telaLogin.setFrameShape(QFrame.Shape.StyledPanel)
        self.telaLogin.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_CineFilmes = QLabel(self.telaLogin)
        self.txt_CineFilmes.setObjectName(u"txt_CineFilmes")
        self.txt_CineFilmes.setGeometry(QRect(20, 20, 161, 31))
        self.txt_CineFilmes.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.txt_Login = QLabel(self.telaLogin)
        self.txt_Login.setObjectName(u"txt_Login")
        self.txt_Login.setGeometry(QRect(20, 110, 121, 41))
        self.txt_Login.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";")
        self.txt_Usuario = QLabel(self.telaLogin)
        self.txt_Usuario.setObjectName(u"txt_Usuario")
        self.txt_Usuario.setGeometry(QRect(20, 170, 49, 16))
        self.txt_Usuario.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Senha = QLabel(self.telaLogin)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(20, 240, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Entrar = QPushButton(self.telaLogin)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(60, 340, 141, 31))
        self.btn_Entrar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Usuario = QLineEdit(self.telaLogin)
        self.btn_Usuario.setObjectName(u"btn_Usuario")
        self.btn_Usuario.setGeometry(QRect(20, 190, 221, 31))
        self.btn_Usuario.setStyleSheet(u"background-color: rgb(244, 248, 255);")
        self.btn_Senha = QLineEdit(self.telaLogin)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(20, 260, 221, 31))
        self.btn_Senha.setStyleSheet(u"background-color: rgb(244, 248, 255);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(60, 50, 821, 511))
        self.img.setPixmap(QPixmap(u":/img/icon/marvel.jpg"))
        self.img.setScaledContents(True)
        Login.setCentralWidget(self.centralwidget)
        self.img.raise_()
        self.telaLogin.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.txt_CineFilmes.setText(QCoreApplication.translate("Login", u"CineFilmes", None))
        self.txt_Login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.txt_Usuario.setText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_Senha.setText(QCoreApplication.translate("Login", u"Senha", None))
        self.btn_Entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.btn_Usuario.setText("")
        self.btn_Senha.setText("")
        self.img.setText("")
    # retranslateUi

import login, sys
from login import Ui_Login
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())