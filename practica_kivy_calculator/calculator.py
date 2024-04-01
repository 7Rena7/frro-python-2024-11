import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class Calculator(App):
    label = ""
    operator = ""
    firstTerm = ""
    secondTerm = ""

    def presser(self, btn):
        if btn == "CE":
            self.erase_label()
            self.operator = ""
            self.firstTerm = ""
            self.secondTerm = ""
            return

        if btn in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            self.update_label(btn)
            return

        # Button is an operator
        if btn == "+":
            if self.secondTerm:
                return
            if self.operator == "+":
                return
            if self.operator != "":
                self.clear_operator()
            self.firstTerm = self.label
            self.operator = "+"
            self.force_update_label(self.label + " + ")
            return

        if btn == "-":
            if self.secondTerm:
                return
            if self.operator == "-":
                return
            if self.operator != "":
                self.clear_operator()
            self.firstTerm = self.label
            self.operator = "-"
            self.force_update_label(self.label + " - ")
            return

        if btn == "×":
            if self.secondTerm:
                return
            if self.operator == "x":
                return
            if self.operator != "":
                self.clear_operator()
            self.firstTerm = self.label
            self.operator = "x"
            self.force_update_label(self.label + " x ")
            return

        if btn == "÷":
            if self.secondTerm:
                return
            if self.operator == "÷":
                return
            if self.operator != "":
                self.clear_operator()
            self.firstTerm = self.label
            self.operator = "÷"
            self.force_update_label(self.label + " ÷ ")
            return

        if btn == "=":
            if not self.secondTerm:
                return
            if self.operator == "÷" and self.secondTerm == "0":
                self.erase_label()
                self.operator = ""
                self.firstTerm = ""
                self.secondTerm = ""
                self.root.ids.label.text = "Error"
                return

            # self.secondTerm = self.label
            operator = self.operator
            if operator == "x": operator = "*"
            if operator == "÷": operator = "/"
            self.label = str(int(eval(self.firstTerm + operator + self.secondTerm)))
            self.root.ids.label.text = self.label
            self.firstTerm = self.label
            self.secondTerm = ""
            self.clear_operator()
            return

    def erase_label(self):
        self.label = ""
        self.root.ids.label.text = self.label

    def update_label(self, value):
        if self.label == "0":
            return
        if self.operator == "":
            self.label = self.label + value
            self.root.ids.label.text = self.label
        if self.firstTerm:
            if self.secondTerm == "0":
                return
            self.secondTerm = self.secondTerm + value
            self.root.ids.label.text = self.label + value

    def force_update_label(self, value):
        self.label = value
        self.root.ids.label.text = self.label

    def clear_operator(self):a
        self.operator = ""
        self.label = self.firstTerm


if __name__ == '__main__':
    Calculator().run()
