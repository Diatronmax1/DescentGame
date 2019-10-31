from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QGridLayout, QPushButton, QTextEdit, QWidget

class SplashScreen(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        newGameBut = QPushButton('New Game')
        loadGameBut = QPushButton('Load Game')
        prefBut = QPushButton('Preferences')
        helpBut = QPushButton('Help')
        #Main Screen
        displayInfo = QTextEdit()
        layout = QGridLayout(self)
        layout.addWidget(newGameBut,        0, 0)
        layout.addWidget(loadGameBut,       1, 0)
        layout.addWidget(prefBut,           2, 0)
        layout.addWidget(helpBut,           3, 0)
        layout.addWidget(displayInfo,       0, 1, 4, 1)
