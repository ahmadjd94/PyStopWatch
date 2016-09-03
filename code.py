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
        MainWindow.resize(400, 499)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 100, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 130, 80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 160, 80, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 0, 381, 91))
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhTime)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(10, 200, 361, 241))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 19))
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.pushButton_3.setText(_translate("MainWindow", "PAUSE"))
        self.label.setText(_translate("MainWindow", "session name"))


def count():

    while Publics.__flag__:
            ThreadLock.acquire()
            ui.lcdNumber.display(str(datetime.datetime.now() - now).split('.')[0])
            # self.lcdNumber.display(str(datetime.datetime.now()-now))
            ThreadLock.release()
            time.sleep(1)
    sessiontime =datetime.datetime.now()
    print ('exiting')

class Publics :
     __flag__=True
     __now__=None
def setup(function):
    if function=='stop':
        pass
    elif function =='pause':
        pass

def starter ():

    if not threads[0].is_alive():
        Publics.__now__ = datetime.datetime.now()
        collection.log.insert ({'name':ui.lineEdit.text(),'starttime':Publics.__now__,'status':'current'})
        ui.lineEdit.setEnabled(False)
        Publics.__flag__=True
        threads[0].start()
    else :
        threads[0].run()
def stop () :
    #threads[0].join()
    ThreadLock.acquire()
    collection.log.update({'starttime':Publics.__now__},{'status':'stopped'})
    Publics.__flag__=False

    ThreadLock.release()
if __name__ == "__main__":

    client =MongoClient() # initialize connection
    collection=client.log  #initialize connection
    ThreadLock= Lock()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    threads = [Thread(target=count,daemon=True),Thread(target=stop,daemon=True)]
    sets=collection.log.find()
    row=sets.count()
    print(row)
    a=sets.next()
    # while a :
    #     ui.tableView.setCurrentIndex(a)
    #     a = sets.next()

    # t2 = Thread(ui.stop, daemon=False)
    sys.exit(app.exec_())



