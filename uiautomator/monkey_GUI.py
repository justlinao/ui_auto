# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monkey.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from monkey_command import monkey


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(346, 484)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 50, 71, 81))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 171, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 90, 171, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 171, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 110, 171, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 50, 61, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 90, 61, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(30, 110, 61, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 130, 141, 31))
        self.checkBox.setObjectName("checkBox")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(35, 161, 291, 301))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.startmonkey)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # 编写自己的槽函数
    def startmonkey(self):
        try:
            packageName = self.lineEdit.text()
            count = self.lineEdit_3.text()
            seed = self.lineEdit_2.text()
            throttle = self.lineEdit_4.text()
            random = self.checkBox.isChecked()
            report = monkey(packageName=packageName, count=count, seed=seed, throttle=throttle, random=random)
            self.textBrowser.setText(report)
        except:
            print("error")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "执行"))
        self.lineEdit_5.setText(_translate("Form", "包名"))
        self.lineEdit_6.setText(_translate("Form", "事件次数"))
        self.lineEdit_7.setText(_translate("Form", "种子数"))
        self.lineEdit_8.setText(_translate("Form", "间隔时间"))
        self.checkBox.setText(_translate("Form", "间隔时间是否随机"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ui_Form()
    w = QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
