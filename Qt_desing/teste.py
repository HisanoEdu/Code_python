import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from Loginfoto import Ui_MainWindow  # Importando o arquivo gerado pelo pyside6-uic (login.ui)
from formulário import Ui_MainWindow  # Importando o arquivo gerado pelo pyside6-uic (formulario.ui)

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a interface do login
        self.login_button.clicked.connect(self.check_login)

    def check_login(self):
        usuario = self.usuario_input.text()
        senha = self.senha_input.text()

        # Verifique as credenciais aqui (exemplo simples)
        if usuario == "eduarda" and senha == "senha123":
            self.close()  # Fecha a janela de login
            self.show_formulario()  # Chama o formulário
        else:
            print("Credenciais inválidas!")

    def show_formulario(self):
        self.formulario_window = QDialog()  # Cria a janela do formulário
        self.formulario_ui = Ui_MainWindow()  # Configura a interface do formulário
        self.formulario_ui.setupUi(self.formulario_window)
        self.formulario_window.exec_()  # Exibe a janela do formulário

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()  # Exibe a tela de login
    sys.exit(app.exec())  # Inicia o loop da aplicação
