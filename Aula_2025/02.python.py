
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olá Mundo")
        self.setGeometry(150, 80, 300, 100)  

        label = QLabel("Hello world", self)
        label.setStyleSheet("font-size: 18px; font-weight: bold;")  
        label.setAlignment(Qt.AlignCenter) 
        
        self.setCentralWidget(label)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = HelloWorldWindow()
    window.show()

    sys.exit(app.exec())


