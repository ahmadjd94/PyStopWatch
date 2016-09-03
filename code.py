# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import datetime
from pymongo import MongoClient
from threading import Thread ,Lock

import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 157)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 5, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 34, 80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 64, 80, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 311, 91))
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhDate | QtCore.Qt.ImhTime)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(16)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.pushButton.clicked.connect(starter)
        self.pushButton_2.clicked.connect(stop)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






    def retranslateUi(self, MainWindow):
        flag=True

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.pushButton_3.setText(_translate("MainWindow", "PAUSE"))

def count():

    while Flag.__flag__:
            ThreadLock.acquire()
            ui.lcdNumber.display(str(datetime.datetime.now() - now).split('.')[0])
            # self.lcdNumber.display(str(datetime.datetime.now()-now))
            ThreadLock.release()
            time.sleep(1)
    sessiontime =datetime.datetime.now()
    print ('exiting')

class Flag :
     __flag__=True
def setup(function):
    if function=='stop':
        pass
    elif function =='pause':
        pass

def starter ():
    if not threads[0].is_alive():
        Flag.__flag__=True
        threads[0].start()
    else :
        threads[0].run()
def stop () :
    #threads[0].join()
    ThreadLock.acquire()
    Flag.__flag__=False

    ThreadLock.release()
if __name__ == "__main__":

    client =MongoClient() # initialize connection
    a=client.log  #initialize connection


    ThreadLock= Lock()
    now = datetime.datetime.now()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    threads = [Thread(target=count,daemon=True),Thread(target=stop,daemon=True)]

    # t2 = Thread(ui.stop, daemon=False)
    sys.exit(app.exec_())



