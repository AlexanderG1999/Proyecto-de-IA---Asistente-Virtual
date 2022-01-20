import sys
from interface import *
from PyQt5.QtWidgets import *

class Ventana(QtWidgets.QMainWindow):  #this = self
    def __init__(self, parent = None):
        super(Ventana,self).__init__(parent=parent)
        self.ui = Ui_MainWindow() #nombre de la clase interface
        self.ui.setupUi(self)
        self.ui.AceptarButton.clicked.connect(self.sumar) #linkea evento
    def sumar (self):
        n1 = int(self.ui.Num1TextEdit.toPlainText()) #getext
        n2 = int(self.ui.Num2TextEdit.toPlainText())
        suma = n1+n2
        self.ui.ResultadoplainTextEdit.setPlainText(str(suma)) # setext

if __name__ == "__main__":
    mi_aplicacion = QtWidgets.QApplication(sys.argv)
    mi_app = Ventana()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
