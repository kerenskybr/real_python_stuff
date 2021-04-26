"""Main Window-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel,QTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('bla bla bla')
        self.setCentralWidget(QTextEdit(acceptRichText=True, tabStopDistance=10))
        self.setGeometry(100, 80, 300, 300)
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("oi eu sou uma barra de status sem status duh")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())