
from PyQt4 import QtCore, QtGui
from mainWindowUi import Ui_MainWindow


class Frontend(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)




if __name__ == "__main__":
    import sys
    a = QtGui.QApplication(sys.argv)
    w = Frontend()
    w.show()
    a.exec_()
