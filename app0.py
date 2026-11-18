import sys 
from PySide6.QtWidgets import (QApplication, QLabel)

app = QApplication(sys.argv)

rotulo = QLabel('Olá, PYside6!')
rotulo.show()

app.exec()