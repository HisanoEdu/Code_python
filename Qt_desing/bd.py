import sys
import Pyside6.Qwidget import QApplication,QWidget,QFileDialog
from Pyside6.QtGui import QPixmap
from ui_tela import ui_form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui.setupUI(self)
        self.ui.Open_btn.clicked.connect(self.open_image)

    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ =file_dialog.getOpenFileNmae(self,"Open Image", "","Images (*.png *.xpm *jpeg *.bmp);;All files(*)")

        if file_path:
            pixmap = QPixmap(file_path)
            self.ui.image.setPixmap(pixmap)
            self.ui.image.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    