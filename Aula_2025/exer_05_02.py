
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olá Mundo")
        self.setGeometry(150, 80, 300, 100)  

        label = QLabel("Hello world", self)
        label.setGeometry(50, 20, 200, 60)  
        label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignCenter)  

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = HelloWorldWindow()
    window.show()

    sys.exit(app.exec())
