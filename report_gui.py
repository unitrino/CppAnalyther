# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created: Wed Feb 05 15:33:18 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(673, 578)
        self.text_Errors = QtGui.QTextEdit(Dialog)
        self.text_Errors.setGeometry(QtCore.QRect(30, 10, 621, 491))
        self.text_Errors.setObjectName(_fromUtf8("text_Errors"))
        self.Button_OK = QtGui.QPushButton(Dialog)
        self.Button_OK.setGeometry(QtCore.QRect(150, 520, 75, 23))
        self.Button_OK.setObjectName(_fromUtf8("Button_OK"))
        self.Button_Sohranit = QtGui.QPushButton(Dialog)
        self.Button_Sohranit.setGeometry(QtCore.QRect(420, 520, 121, 23))
        self.Button_Sohranit.setObjectName(_fromUtf8("Button_Sohranit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Результат анализа", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_OK.setText(QtGui.QApplication.translate("Dialog", "ОК", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Sohranit.setText(QtGui.QApplication.translate("Dialog", "Сохранить отчет", None, QtGui.QApplication.UnicodeUTF8))

