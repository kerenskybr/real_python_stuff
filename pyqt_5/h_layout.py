# Filename: h_layout.py


"""Horizontal layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')

# Creates a layout horizontal
layout = QHBoxLayout()

# Creates a layout vertical
layout = QVBoxLayout()

# Add buttons to layout
#layout.addWidget(QPushButton('Left'))
#layout.addWidget(QPushButton('Center'))
#layout.addWidget(QPushButton('Right'))
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))

# Set the window as layout
window.setLayout(layout)
window.show()

sys.exit(app.exec_())