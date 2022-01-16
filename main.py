from PyQt6 import QtWidgets
from sys import argv

from ui import Ui_MainWindow

basic_operators = "+-*//%."
numbers = "0123456789"
previous_value = str()
answer_calculated = False


class PyUCalculator(Ui_MainWindow):

    def __init__(self, window):
        self.setupUi(window)

        self.btn_clear.clicked.connect(lambda: self.calculate("X"))
        self.btn_allClear.clicked.connect(lambda: self.label_input.setText(
            "0") or self.label_solution.setText("0"))
        self.btn_divide.clicked.connect(lambda: self.calculate("/"))
        self.btn_multiply.clicked.connect(
            lambda: self.calculate("*"))
        self.btn_plus.clicked.connect(
            lambda: self.calculate("+"))
        self.btn_minus.clicked.connect(
            lambda: self.calculate("-"))
        self.btn_mod.clicked.connect(
            lambda: self.calculate("%"))
        self.btn_intDiv.clicked.connect(
            lambda: self.calculate("//"))
        self.btn_equals.clicked.connect(
            lambda: self.calculate("="))
        self.btn_decimal.clicked.connect(
            lambda: self.calculate("."))

        self.btn_0.clicked.connect(lambda: self.calculate("0"))
        self.btn_1.clicked.connect(lambda: self.calculate("1"))
        self.btn_2.clicked.connect(lambda: self.calculate("2"))
        self.btn_3.clicked.connect(lambda: self.calculate("3"))
        self.btn_4.clicked.connect(lambda: self.calculate("4"))
        self.btn_5.clicked.connect(lambda: self.calculate("5"))
        self.btn_6.clicked.connect(lambda: self.calculate("6"))
        self.btn_7.clicked.connect(lambda: self.calculate("7"))
        self.btn_8.clicked.connect(lambda: self.calculate("8"))
        self.btn_9.clicked.connect(lambda: self.calculate("9"))

    def update_solution(self):
        if self.label_input.text()[-1] in numbers:
            try:
                self.label_solution.setText(str(eval(self.label_input.text())))
            except ZeroDivisionError:
                self.label_solution.setText("Zero Division Error")
        else:
            try:
                self.label_solution.setText(
                    str(eval(self.label_input.text()[:-1])))
            except:
                self.label_solution.setText(
                    str(eval(self.label_input.text()[:-2])))

    def calculate(self, user_input):
        global answer_calculated

        if answer_calculated:
            answer_calculated = False
            self.label_input.setText("0")

        if user_input == "=" and self.label_input.text()[-1] not in basic_operators:
            try:
                self.label_input.setText(str(eval(self.label_input.text())))
                answer_calculated = True

            except ZeroDivisionError:
                self.label_solution.setText("Zero Division Error")

        elif user_input == "X":
            self.label_input.setText(self.label_input.text()[:-1])
            if self.label_input.text() == "":
                self.label_input.setText("0")
            self.update_solution()

        elif user_input != "=":
            if (self.label_input.text() == "0" and user_input in numbers):
                self.label_input.clear()
                self.label_input.setText(self.label_input.text() + user_input)
                self.update_solution()

            elif self.label_input.text()[-1] in basic_operators and user_input in basic_operators:
                pass

            else:
                self.label_input.setText(self.label_input.text() + user_input)
                self.update_solution()


app = QtWidgets.QApplication(argv)
MainWindow = QtWidgets.QMainWindow()
ui = PyUCalculator(MainWindow)
MainWindow.show()
app.exec()
