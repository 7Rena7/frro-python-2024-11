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
        # print(btn)
        if btn == "CE":
            self.borrar_label()
            return

        if btn in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            print("El botón presionado fue un número " + btn)
            self.actualizarLabel(btn)
            return

        # Button is an operator
        # Build a switch statement
        if btn == "+":
            self.firstTerm = self.label
            self.operator = "+"
            self.borrar_label()
            return

        if btn == "-":
            self.firstTerm = self.label
            self.operator = "-"
            self.borrar_label()
            return

        if btn == "×":
            self.firstTerm = self.label
            self.operator = "*"
            self.borrar_label()
            return

        if btn == "÷":
            self.firstTerm = self.label
            self.operator = "/"
            self.borrar_label()
            return

        if btn == "=":
            self.secondTerm = self.label
            self.label = str(int(eval(self.firstTerm + self.operator + self.secondTerm)))
            self.root.ids.label.text = self.label
            return


    def borrar_label(self):
        self.label = ""
        self.root.ids.label.text = self.label

    def actualizarLabel(self, value):
        if self.label == "0":
            return
        self.label = self.label + value
        self.root.ids.label.text = self.label
        print(self.label)
        print(type(self.label))


if __name__ == '__main__':
    Calculator().run()
