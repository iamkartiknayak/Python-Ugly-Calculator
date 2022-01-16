from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 515)
        MainWindow.setStyleSheet("background-color:black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(0, 0, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(24)
        self.label_input.setFont(font)
        self.label_input.setStyleSheet("color:white;\n"
                                       "")
        self.label_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                      QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_input.setWordWrap(True)
        self.label_input.setIndent(4)
        self.label_input.setObjectName("label_input")
        self.label_solution = QtWidgets.QLabel(self.centralwidget)
        self.label_solution.setGeometry(QtCore.QRect(0, 70, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_solution.setFont(font)
        self.label_solution.setStyleSheet("color:grey;\n"
                                          "background-color:black;")
        self.label_solution.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_solution.setIndent(6)
        self.label_solution.setObjectName("label_solution")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(3, 139, 325, 355))
        self.groupBox.setStyleSheet("border-style: outset;\n"
                                    "border-width:1px;\n"
                                    "border-radius: 6px;\n"
                                    "border-color: grey;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_7 = QtWidgets.QPushButton(self.groupBox)
        self.btn_7.setGeometry(QtCore.QRect(10, 10, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_7.setDefault(False)
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.groupBox)
        self.btn_8.setGeometry(QtCore.QRect(90, 10, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_8.setDefault(False)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.groupBox)
        self.btn_9.setGeometry(QtCore.QRect(170, 10, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_9.setDefault(False)
        self.btn_9.setObjectName("btn_9")
        self.btn_divide = QtWidgets.QPushButton(self.groupBox)
        self.btn_divide.setGeometry(QtCore.QRect(250, 80, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_divide.setFont(font)
        self.btn_divide.setAutoFillBackground(False)
        self.btn_divide.setStyleSheet("color:lightgreen;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: grey;")
        self.btn_divide.setAutoDefault(False)
        self.btn_divide.setDefault(False)
        self.btn_divide.setFlat(False)
        self.btn_divide.setObjectName("btn_divide")
        self.btn_4 = QtWidgets.QPushButton(self.groupBox)
        self.btn_4.setGeometry(QtCore.QRect(10, 80, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_4.setDefault(False)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.groupBox)
        self.btn_5.setGeometry(QtCore.QRect(90, 80, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_5.setDefault(False)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.groupBox)
        self.btn_6.setGeometry(QtCore.QRect(170, 80, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_6.setDefault(False)
        self.btn_6.setObjectName("btn_6")
        self.btn_multiply = QtWidgets.QPushButton(self.groupBox)
        self.btn_multiply.setGeometry(QtCore.QRect(250, 150, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet("color:lightgreen;\n"
                                        "border-style: outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: grey;")
        self.btn_multiply.setDefault(False)
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_1 = QtWidgets.QPushButton(self.groupBox)
        self.btn_1.setGeometry(QtCore.QRect(10, 150, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_1.setDefault(False)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_2.setGeometry(QtCore.QRect(90, 150, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_2.setDefault(False)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.groupBox)
        self.btn_3.setGeometry(QtCore.QRect(170, 150, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_3.setDefault(False)
        self.btn_3.setObjectName("btn_3")
        self.btn_plus = QtWidgets.QPushButton(self.groupBox)
        self.btn_plus.setGeometry(QtCore.QRect(250, 220, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("color:lightgreen;\n"
                                    "border-style: outset;\n"
                                    "border-width:2px;\n"
                                    "border-radius: 10px;\n"
                                    "border-color: grey;")
        self.btn_plus.setDefault(False)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.groupBox)
        self.btn_minus.setGeometry(QtCore.QRect(250, 290, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("color:lightgreen;\n"
                                     "border-style: outset;\n"
                                     "border-width:2px;\n"
                                     "border-radius: 10px;\n"
                                     "border-color: grey;")
        self.btn_minus.setDefault(False)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_equals = QtWidgets.QPushButton(self.groupBox)
        self.btn_equals.setGeometry(QtCore.QRect(10, 290, 145, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(26)
        self.btn_equals.setFont(font)
        self.btn_equals.setStyleSheet("color:yellow;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: grey;")
        self.btn_equals.setDefault(False)
        self.btn_equals.setObjectName("btn_equals")
        self.btn_0 = QtWidgets.QPushButton(self.groupBox)
        self.btn_0.setGeometry(QtCore.QRect(94, 220, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("color:white;\n"
                                 "border-style: outset;\n"
                                 "border-width:2px;\n"
                                 "border-radius: 10px;\n"
                                 "border-color: grey;")
        self.btn_0.setDefault(False)
        self.btn_0.setObjectName("btn_0")
        self.btn_allClear = QtWidgets.QPushButton(self.groupBox)
        self.btn_allClear.setGeometry(QtCore.QRect(250, 10, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_allClear.setFont(font)
        self.btn_allClear.setStyleSheet("color:red;\n"
                                        "border-style: outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: grey;")
        self.btn_allClear.setDefault(False)
        self.btn_allClear.setObjectName("btn_allClear")
        self.btn_intDiv = QtWidgets.QPushButton(self.groupBox)
        self.btn_intDiv.setGeometry(QtCore.QRect(170, 290, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_intDiv.setFont(font)
        self.btn_intDiv.setStyleSheet("color:lightgreen;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: grey;")
        self.btn_intDiv.setDefault(False)
        self.btn_intDiv.setObjectName("btn_intDiv")
        self.btn_decimal = QtWidgets.QPushButton(self.groupBox)
        self.btn_decimal.setGeometry(QtCore.QRect(10, 220, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(26)
        self.btn_decimal.setFont(font)
        self.btn_decimal.setStyleSheet("color:lightgreen;\n"
                                       "border-style: outset;\n"
                                       "border-width:2px;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: grey;")
        self.btn_decimal.setDefault(False)
        self.btn_decimal.setObjectName("btn_decimal")
        self.btn_mod = QtWidgets.QPushButton(self.groupBox)
        self.btn_mod.setGeometry(QtCore.QRect(170, 220, 65, 55))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.btn_mod.setFont(font)
        self.btn_mod.setStyleSheet("color:lightgreen;\n"
                                   "border-style: outset;\n"
                                   "border-width:2px;\n"
                                   "border-radius: 10px;\n"
                                   "border-color: grey;")
        self.btn_mod.setDefault(False)
        self.btn_mod.setObjectName("btn_mod")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(280, 110, 41, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("color:red;\n"
                                     "border-style: outset;\n"
                                     "border-width:2px;\n"
                                     "border-radius: 10px;\n"
                                     "border-color: grey;")
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyU Calculator"))
        self.label_input.setText(_translate("MainWindow", "0"))
        self.label_solution.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_divide.setText(_translate("MainWindow", "÷"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_multiply.setText(_translate("MainWindow", "x"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_equals.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_allClear.setText(_translate("MainWindow", "C"))
        self.btn_intDiv.setText(_translate("MainWindow", "//"))
        self.btn_decimal.setText(_translate("MainWindow", " . "))
        self.btn_mod.setText(_translate("MainWindow", "%"))
        self.btn_clear.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
