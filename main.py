import sys
import math
import tempfile
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from views.ensayator_ui import Ui_MainWindow
from views.models.table_models import TableModel
from dialogs.in_progress_dialog import InProgressDialog
from workers.preview import PreviewTaskThread
from workers.calculate import CalculateTaskThread
from core.excel_logic import ExcelLogic
import time
from datetime import datetime
from views.app_icon import create_app_icon
import PyQt5.sip


class Ensayator(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        icon = create_app_icon()
        MainWindow.setWindowIcon(icon)
        self.btnLoadFile.clicked.connect(self.load_file)
        self.btnCalc.clicked.connect(self.execute_calc)
        self.sbTotalEnsay.valueChanged.connect(self.calc_cycles)
        self.cbEnableRepetitions.stateChanged.connect(self.set_repetitions_state)
        self.txtCycles.setReadOnly(True)
        self.pbProgress.setVisible(False)
        self.lblEtaTitle.setVisible(False)
        self.lblEta.setVisible(False)
        self.lblDuration.setVisible(False)
        self.lblDurationTitle.setVisible(False)
        self.file = None
        self.p_dialog = None
        self.previewWorker = None
        self.calcWorker = None
        self.el = None
        self.ensayRows = []
        self.startCalcAt = None
        self.set_input_state(False, False)
        self.intervalSet = False

    def calc_cycles(self):
        try:
            nw_time = self.sbTotalEnsay.value()
            minutes = nw_time * 60
            cycles = int(math.ceil(minutes / self.sbDuration.value()))
            self.txtCycles.setText(str(cycles))
            if cycles > 0:
                self.btnCalc.setEnabled(True)
        except:
            self.txtCycles.setText(str(0))

    def set_input_state(self, state, calc_state=False):
        self.cbEnableRepetitions.setEnabled(state)
        self.cbSelectColumn.setEnabled(state)
        self.sbTotalEnsay.setEnabled(state)
        self.sbOffset.setEnabled(state)
        self.sbDuration.setEnabled(state)
        self.txtOutName.setEnabled(state)
        self.btnCalc.setEnabled(calc_state)
        self.txtCycles.setEnabled(state)

    def set_repetitions_state(self):
        state = self.cbEnableRepetitions.isChecked()
        self.lblRepetitions.setEnabled(state)
        self.lblWaiting.setEnabled(state)
        self.lblWaitingUnit.setEnabled(state)
        self.sbRepetitions.setEnabled(state)
        self.sbWaiting.setEnabled(state)

    def load_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, "Seleccionar Excel", "", "Excel (*.xlsx)", options=options)
        if file_name:
            self.set_input_state(False, False)
            self.txtOutName.setText(file_name.split("/")[-1].replace(".xlsx", ""))
            self.el = ExcelLogic(file_name)
            self.file = file_name
            self.lblFilePath.setText(file_name)
            self.start_preview()

    def start_preview(self):
        self.p_dialog = InProgressDialog(self.centralwidget)
        self.p_dialog.show()
        # and pass your argumetn to it's constructor here
        self.previewWorker = PreviewTaskThread(mw=self)
        self.previewWorker.finished.connect(self.finished_preview)
        self.previewWorker.start()

    def finished_preview(self):
        self.tblPreview.reset()
        model = TableModel(self.el.preview)
        self.tblPreview.setModel(model)
        self.p_dialog.close()
        for cl in self.el.preview[0]:
            self.cbSelectColumn.addItem(cl)
        self.set_input_state(True, False)

    def execute_calc(self):
        self.intervalSet = False
        self.set_input_state(False, False)
        self.lblDuration.setVisible(True)
        self.lblDurationTitle.setVisible(True)
        self.lblDuration.setText("00:00:00")
        self.lblEtaTitle.setVisible(True)
        self.lblEta.setVisible(True)
        self.lblEta.setText("ND")
        self.startCalcAt = datetime.now()
        self.pbProgress.setValue(0)
        self.pbProgress.setVisible(True)
        self.calcWorker = CalculateTaskThread(mw=self)
        self.calcWorker.notifyProgress.connect(self.calculate_signal_accept)
        self.calcWorker.finished.connect(self.finished_calc)
        self.calcWorker.start()

    def finished_calc(self):
        self.set_input_state(True, True)
        self.set_table_intervals(self.ensayRows)

    def calculate_signal_accept(self, msg):
        if not self.intervalSet:
            self.set_table_intervals(msg[1])

        progress = int(msg[0])
        self.pbProgress.setValue(progress)
        current = datetime.now()
        st_time = time.mktime(self.startCalcAt.timetuple())
        nd_time = time.mktime(current.timetuple())

        elapsed = int(nd_time - st_time)
        self.lblDuration.setText(time.strftime('%H:%M:%S', time.gmtime(elapsed)))

        if progress > 0:
            remaining = ((elapsed * 100) / progress) - elapsed
            self.lblEta.setText(time.strftime('%H:%M:%S', time.gmtime(remaining)))

    def set_table_intervals(self, ensay_rows):
        self.intervalSet = True
        out_rows = [["#", "SIN MARGEN", "START", "END", "DURATION"]]
        for num, ors in enumerate(ensay_rows):
            st_rw = ors[0]
            nd_rw = ors[1]
            st_time = time.mktime(st_rw.timetuple())
            nd_time = time.mktime(nd_rw.timetuple())
            dur = int(nd_time - st_time) / 60
            out_rows.append([num + 1, ors[2].strftime("%Y/%m/%d %H:%M:%S"), ors[0].strftime("%Y/%m/%d %H:%M:%S"), ors[1].strftime("%Y/%m/%d %H:%M:%S"), dur])

        model = TableModel(out_rows)
        self.tblPreview.setModel(model)


if __name__ == '__main__':
    sys.stdout = tempfile.TemporaryFile()
    sys.stderr = tempfile.TemporaryFile()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    pos = Ensayator(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
