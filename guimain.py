import sys

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QApplication

from lib import descentmodel
from qtlib import splash

class DescentGameWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.splashScreen = splash.SplashScreen()
        self.setCentralWidget(self.splashScreen)
        self.show()
        #Game shouldn't be initialized until splash screen is complete
        #self.model = descentmodel.DescentGame()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DescentGameWindow()
    sys.exit(app.exec_())