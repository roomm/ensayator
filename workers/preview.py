from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore


class PreviewTaskThread(QtCore.QThread):
    notifyProgress = QtCore.pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, mw, parent=None):
        QThread.__init__(self, parent)
        self.mw = mw

    def run(self):
        self.mw.el.load_preview()
        self.finished.emit()
