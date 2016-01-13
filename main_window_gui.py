# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Wed Feb 05 15:32:48 2014
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
        Dialog.resize(472, 237)
        self.Button_Vibor_Faila = QtGui.QPushButton(Dialog)
        self.Button_Vibor_Faila.setGeometry(QtCore.QRect(70, 80, 141, 81))
        self.Button_Vibor_Faila.setObjectName(_fromUtf8("Button_Vibor_Faila"))
        self.Button_Exit = QtGui.QPushButton(Dialog)
        self.Button_Exit.setGeometry(QtCore.QRect(270, 80, 141, 81))
        self.Button_Exit.setObjectName(_fromUtf8("Button_Exit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Программа поиска уязвимостей программного кода", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Vibor_Faila.setText(QtGui.QApplication.translate("Dialog", "Выбрать файл", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Exit.setText(QtGui.QApplication.translate("Dialog", "Выход", None, QtGui.QApplication.UnicodeUTF8))

