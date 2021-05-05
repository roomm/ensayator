from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore


class CalculateTaskThread(QtCore.QThread):
    notifyProgress = QtCore.pyqtSignal(object)
    task_failed = QtCore.pyqtSignal(object)
    finished = pyqtSignal()

    def __init__(self, mw, parent=None):
        QThread.__init__(self, parent)
        self.mw = mw

    def run(self):
        result = None
        try:
            result = self.mw.el.calculate_ensys(
                self.mw.cbSelectColumn.currentText(),
                self.mw.sbScale.value(),
                self.mw.sbDuration.value(),
                self.mw.sbOffset.value(),
                int(self.mw.txtCycles.text()),
                self.mw.txtOutName.text(),
                self.notifyProgress,
                self.task_failed
            )
        except Exception as e:
            self.task_failed.emit(str(e))
        if result:
            self.mw.ensayRows = result
            self.finished.emit()
