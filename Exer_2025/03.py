
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Hello World')

    layout = QVBoxLayout()

    name_label = QLabel('Eduarda Hisano')
    name_label.setAlignment(Qt.AlignCenter)

    image_label = QLabel()
    pixmap = QPixmap('C:/Users/Imagens/Downloads/eduarda.jpg')  
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)

    layout.addWidget(name_label)
    layout.addWidget(image_label)

    window.setLayout(layout)

    window.resize(400, 400) 

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
