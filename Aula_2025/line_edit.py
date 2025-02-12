
import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
 
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.setWindowTitle("Login")
 
        self.label_username = QLabel("Usuário:")
        self.input_username = QLineEdit()
 
        self.label_password = QLabel("Senha:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
 
        self.button_login = QPushButton("Entrar")
        self.button_login.clicked.connect(self.check_login)
 
 
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)
 
        self.setLayout(layout)
 
    def check_login(self):
        correct_username = "Eduarda"
        correct_password = "senha123"
 
        username = self.input_username.text()
        password = self.input_password.text()
 
        if username == correct_username and password == correct_password:
            QMessageBox.information(self, "Login bem-sucedido", "Bem-vindo, " + username + "!")
        else:
            QMessageBox.warning(self, "Erro no Login", "Usuário ou senha incorretos.")
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

