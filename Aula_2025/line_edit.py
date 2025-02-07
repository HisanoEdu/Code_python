import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ReverseNameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reverter o nome")

        self.label_name = QLabel("Digite seu nome:")
        self.input_name = QLineEdit()
        self.button = QPushButton("Inverter")
        self.result_name = QLabel(" ")

        self.button.clicked.connect(self.reverse_name)

        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button)
        layout.addWidget(self.result_name)

        self.setLayout(layout)  # Define o layout principal da janela

    def reverse_name(self):
        name = self.input_name.text()
        reversed_name = ""  # Corrigido para uma string vazia
        for i in range(len(name) - 1, -1, -1):  # Corrigido o loop
            reversed_name += name[i]  # Adiciona cada caractere na string invertida
        self.result_name.setText(f"Nome invertido: {reversed_name}")  # Atualiza o texto do rótulo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReverseNameWindow()
    window.show()
    sys.exit(app.exec())  # Executa o aplicativo
