import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class Calculator(App):

    label = ""

    def presser(self, btn):
        print(btn)
        if btn == "CE":
            self.aplicarCe()
            return
        if(btn in ["1","2","3","4","5","6","7","8","9","0"]):
            print("El resultado es un numero " + btn)
            self.aplicarNumero(btn)
        else: print("El resultado no es un numero")
        pass

    def aplicarNumero(self, value):
        print(len(self.label))
        print(len(self.label)==0)
        if(True):#self.label == "" and len(self.label)==0):
            self.actualizarLabel(value)

    def aplicarCe(self):
        self.label = ""
        self.root.ids.label.text = self.label

    def actualizarLabel(self,value):
        if(self.label == "0"):
            return
        self.label = self.label + value
        self.root.ids.label.text =self.label

if __name__ == '__main__':
    Calculator().run()

# Button
# Grid Layout
# Label
