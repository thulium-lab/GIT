"""OLD UNUSED PROGRAMM"""

import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy,
                             QLabel, QLineEdit, QPushButton)


class plotWidget(FigureCanvasi):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig, self.axes = plt.subplots()
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        # self.axes2 = fig.add_subplot(111)
        # self.axes.hold(False)
        # self.axes2.hold(False)
        super(plotWidget, self).__init__(fig)
        self.setParent(parent)
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Blue laser lock")
        self.main_widget = QtWidgets.QWidget(self)
        layout1 = QtWidgets.QHBoxLayout(self.main_widget)
        layout1l = plotWidget(self.main_widget)
        layout1r = QtWidgets.QVBoxLayout(self.main_widget)
        connect_btn = QPushButton('Connect',self)
