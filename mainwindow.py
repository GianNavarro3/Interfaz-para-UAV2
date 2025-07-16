# This Python file uses the following encoding: utf-8
import cv2
import time
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage, QPainter, QBrush, QPainterPath
from PySide6.QtCore import QTimer, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        pixmap2 = QPixmap("imagenes/imagen_dron.jpg").scaled(self.ui.labelvideo.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        rounded = rounded_pixmap(pixmap2, radius=12)  # ajusta el radio según tu diseño
        self.ui.labelvideo.setPixmap(rounded)
        self.ui.labelvideo.setScaledContents(True)

        pixmap = QPixmap("imagenes/mapa.png")
        self.ui.mapa.setPixmap(pixmap)
        self.ui.mapa.setScaledContents(True)

def rounded_pixmap(pixmap, radius):
    size = pixmap.size()
    rounded = QPixmap(size)
    rounded.fill(Qt.transparent)

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.Antialiasing)
        
    path = QPainterPath()
    path.addRoundedRect(0, 0, size.width(), size.height(), radius, radius)
        
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
        
    return rounded

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
