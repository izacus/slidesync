# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue May  8 11:49:37 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(250, 373)
        MainWindow.setWindowTitle(_fromUtf8("Viidea Slide Sync"))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Slovenian, QtCore.QLocale.Slovenia))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 361))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 30, 10, 30)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblLoadFiles = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblLoadFiles.setText(QtGui.QApplication.translate("MainWindow", "1. Select files", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoadFiles.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblLoadFiles.setObjectName(_fromUtf8("lblLoadFiles"))
        self.verticalLayout.addWidget(self.lblLoadFiles)
        self.lblExtractFrames = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblExtractFrames.setText(QtGui.QApplication.translate("MainWindow", "2. Extract frames from slide video", None, QtGui.QApplication.UnicodeUTF8))
        self.lblExtractFrames.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblExtractFrames.setObjectName(_fromUtf8("lblExtractFrames"))
        self.verticalLayout.addWidget(self.lblExtractFrames)
        self.lblMatch = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMatch.setText(QtGui.QApplication.translate("MainWindow", "3. Match slides with frames", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMatch.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblMatch.setObjectName(_fromUtf8("lblMatch"))
        self.verticalLayout.addWidget(self.lblMatch)
        self.lblReview = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblReview.setText(QtGui.QApplication.translate("MainWindow", "4. Review matched slides", None, QtGui.QApplication.UnicodeUTF8))
        self.lblReview.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblReview.setObjectName(_fromUtf8("lblReview"))
        self.verticalLayout.addWidget(self.lblReview)
        self.lblSync = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblSync.setText(QtGui.QApplication.translate("MainWindow", "5. Sync slides with main video", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSync.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblSync.setObjectName(_fromUtf8("lblSync"))
        self.verticalLayout.addWidget(self.lblSync)
        self.lblSave = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblSave.setText(QtGui.QApplication.translate("MainWindow", "6. Save slide archive", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSave.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSave.setObjectName(_fromUtf8("lblSave"))
        self.verticalLayout.addWidget(self.lblSave)
        self.btnStart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStart.setDefault(True)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.verticalLayout.addWidget(self.btnStart)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

