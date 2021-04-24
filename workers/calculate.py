from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore


class CalculateTaskThread(QtCore.QThread):
    notifyProgress = QtCore.pyqtSignal(object)
    finished = pyqtSignal()

    def __init__(self, mw, parent=None):
        QThread.__init__(self, parent)
        self.mw = mw

    def run(self):
        self.mw.ensayRows = self.mw.el.calculate_ensys(
            self.mw.cbSelectColumn.currentText(),
            self.mw.sbDuration.value(),
            self.mw.sbOffset.value(),
            self.mw.sbCycles.value(),
            self.mw.txtOutName.text(),
            self.notifyProgress
        )
        self.finished.emit()
