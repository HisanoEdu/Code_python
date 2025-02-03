
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def on_button_click():
    print("Botão clicado!")

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Hello World')

    layout = QVBoxLayout()

    name_label = QLabel('Eduarda Hisano')
    name_label.setAlignment(Qt.AlignCenter)

    image_label = QLabel()
    pixmap = QPixmap('C:/Users/SEU_NOME_DE_USUARIO/Downloads/eduarda.jpg')  
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)

   
    button = QPushButton('Clique aqui')
    button.clicked.connect(on_button_click) 

    layout.addWidget(name_label)
    layout.addWidget(image_label)
    layout.addWidget(button)

    window.setLayout(layout)

    window.resize(400, 500)

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
