# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class InProgressDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InProgressDialog, self).__init__(*args, **kwargs)
        self.setFixedSize(400, 84)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(120, 10, 261, 17))
        self.label.setObjectName("label")

        self.setWindowTitle("Procesando")
        self.label.setText("En proceso...")
