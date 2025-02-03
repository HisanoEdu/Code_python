
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel

def main():
    app = QApplication(sys.argv)


    window = QWidget()
    window.setWindowTitle('Hello World')
    label = QLabel('Hello, World!', parent=window)
    label.move(100, 100)

    window.resize(300, 200)
    
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
