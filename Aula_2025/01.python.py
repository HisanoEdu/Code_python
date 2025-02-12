from PySide6.QtWidgets import QApplication,QLabel,QMainWindow
from PySide6.QtCore import Qt
import sys

class HelloWorlWindow(QMainWindow):
    def __init__ (self):
      super().__init__()

      self.setWindowTitle("Olá Mundo")
      self.setGeometry(150,80,100,30) #x,y

      label =QLabel("Hello world", self)
      label.setGeometry(150,80,100,30)
      label.setStyleSheet("font-size: 18px; font-weight: bold; text-aling: center")

if __name__ == "__main__":
    app=QApplication(sys.argv)

    window = HelloWorlWindow()
    window.show()
    
    sys.exit(app.exec())

