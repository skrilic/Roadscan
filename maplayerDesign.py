# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmz_generator.ui'
#
# Created: Mon Oct 24 14:06:57 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormKmz(object):
    def setupUi(self, FormKmz):
        FormKmz.setObjectName("FormKmz")
        FormKmz.resize(392, 90)
        FormKmz.setMinimumSize(QtCore.QSize(392, 0))
        self.verticalLayout_2 = QtGui.QVBoxLayout(FormKmz)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_input = QtGui.QLabel(FormKmz)
        self.label_input.setObjectName("label_input")
        self.horizontalLayout.addWidget(self.label_input)
        self.toolButton_input = QtGui.QToolButton(FormKmz)
        self.toolButton_input.setObjectName("toolButton_input")
        self.horizontalLayout.addWidget(self.toolButton_input)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_output = QtGui.QLabel(FormKmz)
        self.label_output.setObjectName("label_output")
        self.horizontalLayout.addWidget(self.label_output)
        self.toolButton_output = QtGui.QToolButton(FormKmz)
        self.toolButton_output.setObjectName("toolButton_output")
        self.horizontalLayout.addWidget(self.toolButton_output)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_OK = QtGui.QPushButton(FormKmz)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.horizontalLayout_3.addWidget(self.pushButton_OK)
        self.pushButton_Cancel = QtGui.QPushButton(FormKmz)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_Cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.progressBar = QtGui.QProgressBar(FormKmz)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)

        self.retranslateUi(FormKmz)
        QtCore.QMetaObject.connectSlotsByName(FormKmz)

    def retranslateUi(self, FormKmz):
        FormKmz.setWindowTitle(QtGui.QApplication.translate("FormKmz", "KMZ Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_input.setText(QtGui.QApplication.translate("FormKmz", "Input file: ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_input.setToolTip(QtGui.QApplication.translate("FormKmz", "Select measurement log file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_input.setText(QtGui.QApplication.translate("FormKmz", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_output.setText(QtGui.QApplication.translate("FormKmz", "Output file: ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_output.setToolTip(QtGui.QApplication.translate("FormKmz", "Select the output file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_output.setText(QtGui.QApplication.translate("FormKmz", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_OK.setText(QtGui.QApplication.translate("FormKmz", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setText(QtGui.QApplication.translate("FormKmz", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormKmz = QtGui.QWidget()
    ui = Ui_FormKmz()
    ui.setupUi(FormKmz)
    FormKmz.show()
    sys.exit(app.exec_())

