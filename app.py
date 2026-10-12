from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
import sys 

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        image_path = Path('extension/assets/reze.png')

        self.setWindowTitle("Waifu for Life-u")
        self.setWindowIcon(QIcon(str(image_path)))

        self.pixmap = QPixmap(str(image_path))

        self.pixmap = self.pixmap.scaled(
            300, 
            300,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.label = QLabel(self)
        self.label.setStyleSheet("background: transparent")
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label.adjustSize()
        self.setFixedSize(self.pixmap.size())

        screen = QApplication.primaryScreen().availableGeometry()

        x = screen.right() - self.width() - 20
        y = screen.top() + 20

        self.move(x, y)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())