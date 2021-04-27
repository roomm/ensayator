# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ensayator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 591)
        MainWindow.setMinimumSize(QtCore.QSize(1003, 591))
        MainWindow.setMaximumSize(QtCore.QSize(1003, 591))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadFile.setGeometry(QtCore.QRect(20, 10, 101, 25))
        self.btnLoadFile.setObjectName("btnLoadFile")
        self.lblFilePath = QtWidgets.QLabel(self.centralwidget)
        self.lblFilePath.setGeometry(QtCore.QRect(140, 10, 631, 25))
        self.lblFilePath.setText("")
        self.lblFilePath.setObjectName("lblFilePath")
        self.tblPreview = QtWidgets.QTableView(self.centralwidget)
        self.tblPreview.setGeometry(QtCore.QRect(20, 50, 661, 511))
        self.tblPreview.setObjectName("tblPreview")
        self.cbSelectColumn = QtWidgets.QComboBox(self.centralwidget)
        self.cbSelectColumn.setGeometry(QtCore.QRect(830, 60, 161, 25))
        self.cbSelectColumn.setObjectName("cbSelectColumn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 60, 121, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 100, 121, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 140, 121, 25))
        self.label_4.setObjectName("label_4")
        self.btnCalc = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalc.setGeometry(QtCore.QRect(700, 300, 291, 25))
        self.btnCalc.setObjectName("btnCalc")
        self.pbProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.pbProgress.setGeometry(QtCore.QRect(700, 340, 291, 23))
        self.pbProgress.setProperty("value", 24)
        self.pbProgress.setObjectName("pbProgress")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 180, 121, 25))
        self.label_5.setObjectName("label_5")
        self.sbDuration = QtWidgets.QSpinBox(self.centralwidget)
        self.sbDuration.setGeometry(QtCore.QRect(830, 100, 48, 26))
        self.sbDuration.setObjectName("sbDuration")
        self.sbOffset = QtWidgets.QSpinBox(self.centralwidget)
        self.sbOffset.setGeometry(QtCore.QRect(830, 140, 48, 26))
        self.sbOffset.setObjectName("sbOffset")
        self.txtOutName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOutName.setGeometry(QtCore.QRect(830, 260, 141, 25))
        self.txtOutName.setObjectName("txtOutName")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 260, 121, 25))
        self.label_6.setObjectName("label_6")
        self.lblEta = QtWidgets.QLabel(self.centralwidget)
        self.lblEta.setGeometry(QtCore.QRect(910, 380, 81, 20))
        self.lblEta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblEta.setObjectName("lblEta")
        self.lblEtaTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblEtaTitle.setGeometry(QtCore.QRect(700, 380, 171, 17))
        self.lblEtaTitle.setObjectName("lblEtaTitle")
        self.lblDuration = QtWidgets.QLabel(self.centralwidget)
        self.lblDuration.setGeometry(QtCore.QRect(910, 420, 81, 20))
        self.lblDuration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDuration.setObjectName("lblDuration")
        self.lblDurationTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblDurationTitle.setGeometry(QtCore.QRect(700, 420, 171, 17))
        self.lblDurationTitle.setObjectName("lblDurationTitle")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(960, 550, 41, 17))
        self.label_7.setObjectName("label_7")
        self.sbTotalEnsay = QtWidgets.QSpinBox(self.centralwidget)
        self.sbTotalEnsay.setGeometry(QtCore.QRect(830, 180, 48, 26))
        self.sbTotalEnsay.setObjectName("sbTotalEnsay")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(890, 100, 61, 25))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(890, 140, 61, 25))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(890, 180, 61, 25))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 220, 121, 25))
        self.label_11.setObjectName("label_11")
        self.txtCycles = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCycles.setGeometry(QtCore.QRect(830, 220, 61, 25))
        self.txtCycles.setObjectName("txtCycles")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnLoadFile, self.cbSelectColumn)
        MainWindow.setTabOrder(self.cbSelectColumn, self.sbDuration)
        MainWindow.setTabOrder(self.sbDuration, self.sbOffset)
        MainWindow.setTabOrder(self.sbOffset, self.sbTotalEnsay)
        MainWindow.setTabOrder(self.sbTotalEnsay, self.txtOutName)
        MainWindow.setTabOrder(self.txtOutName, self.btnCalc)
        MainWindow.setTabOrder(self.btnCalc, self.tblPreview)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ensayator"))
        self.btnLoadFile.setText(_translate("MainWindow", "Cargar Excel"))
        self.label_2.setText(_translate("MainWindow", "Columna Master"))
        self.label_3.setText(_translate("MainWindow", "Duracion Ciclo"))
        self.label_4.setText(_translate("MainWindow", "Margen "))
        self.btnCalc.setText(_translate("MainWindow", "Calcular"))
        self.label_5.setText(_translate("MainWindow", "Duracion Ensayo"))
        self.label_6.setText(_translate("MainWindow", "Nombre Salida"))
        self.lblEta.setText(_translate("MainWindow", "00:00:00"))
        self.lblEtaTitle.setText(_translate("MainWindow", "Tiempo restante:"))
        self.lblDuration.setText(_translate("MainWindow", "00:00:00"))
        self.lblDurationTitle.setText(_translate("MainWindow", "Tiempo transcurrido:"))
        self.label_7.setText(_translate("MainWindow", "v1.0.2"))
        self.label_8.setText(_translate("MainWindow", "min"))
        self.label_9.setText(_translate("MainWindow", "min"))
        self.label_10.setText(_translate("MainWindow", "hrs"))
        self.label_11.setText(_translate("MainWindow", "# Cyclos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
