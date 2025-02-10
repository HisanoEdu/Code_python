from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
from register_window import RegisterWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Login")

        self.label_username = QLabel("Usuário:")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Digite seu nome de usuário")

        self.label_password = QLabel("Senha:")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Digite sua senha")
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
        correct_password = "123"

        username = self.input_username.text()
        password = self.input_password.text()

        if username == correct_username and password == correct_password:
            print("Login bem-sucedido! Abrindo tela de cadastro...")
            self.open_register()
        else:
            print("Usuário ou senha inválido.")
    
    def open_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()