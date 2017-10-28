# from PyQt5.QtCore import QObject
import random
import numpy as np
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Qt5Agg',force=True)
from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QPainter)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy,
                             QLabel, QLineEdit, QPushButton)


# FigureCanvas inherits QWidget
class MainWindow(FigureCanvas):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig, self.axes = plt.subplots()
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        # self.axes2 = fig.add_subplot(111)
        # self.axes.hold(False)
        # self.axes2.hold(False)
        super(MainWindow, self).__init__(fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(50)

        self.x = np.array([0])
        self.y = 2 * self.x
        self.z = 3 * self.x

        self.setWindowTitle("Sin Curve")

    def update_figure(self):
        self.x = np.append(self.x, len(self.x))

        self.y = 2 * self.x
        self.z = 3 * self.x

        self.axes.plot(self.x, self.y, 'r-*')
        self.axes.plot(self.x, self.z, 'b-*')
        # self.y = np.roll(self.y,-1)
        self.draw()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())