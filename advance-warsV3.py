#!/usr/bin/env python3

# Filename : advance-wars

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from functools import partial

class AwUI(QMainWindow) :
    def __init__(self) :
        super().___init__()
        self.setWindowTitle('Advance-Wars version 2.0')
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)