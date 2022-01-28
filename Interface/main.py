import sys
from menu import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# mover ventana
		self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

		#acceder a las paginas
		self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))			
		self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
		self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))	
		self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))

		#control barra de titulos
		self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.bt_cerrar.clicked.connect(lambda: self.close())

		self.ui.bt_restaurar.hide()

		#menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)

	def control_bt_minimizar(self):
		self.showMinimized()		


	def  control_bt_normal(self): 
		self.showNormal()		
		self.ui.bt_restaurar.hide()
		self.ui.bt_maximizar.show()
		#Page_Uno
		self.ui.lineEdit.setGeometry(QtCore.QRect(170, 100, 250, 41))
		self.ui.lineEdit_NewProgram.setGeometry(QtCore.QRect(100, 180, 391, 51))
		self.ui.pushButton_NewProg.setGeometry(QtCore.QRect(210, 300, 171, 31))
		#Page_Dos
		self.ui.lineEdit_3.setGeometry(QtCore.QRect(170, 100, 250, 41))
		self.ui.lineEdit_NewMail.setGeometry(QtCore.QRect(100, 190, 391, 51))
		self.ui.pushButton_NewMail.setGeometry(QtCore.QRect(210, 310, 171, 31))
		#Page_Tres
		self.ui.pushButton_NewFaVidComp.setGeometry(QtCore.QRect(90, 130, 400, 41))
		self.ui.pushButton_NewFacCamComp.setGeometry(QtCore.QRect(90, 270, 400, 41))


	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.ui.bt_maximizar.hide()
		self.ui.bt_restaurar.show()
		extender = int((726-self.ui.page_uno.width())/9)
		#Page_Uno
		self.ui.lineEdit.setGeometry(QtCore.QRect(250+extender, 100, 250, 41))
		self.ui.lineEdit_NewProgram.setGeometry(QtCore.QRect(180+extender, 180, 391, 51))
		self.ui.pushButton_NewProg.setGeometry(QtCore.QRect(290+extender, 300, 171, 31))
		#Page_Dos
		self.ui.lineEdit_3.setGeometry(QtCore.QRect(250+extender, 100, 250, 41))
		self.ui.lineEdit_NewMail.setGeometry(QtCore.QRect(180+extender, 190, 391, 51))
		self.ui.pushButton_NewMail.setGeometry(QtCore.QRect(290+extender, 310, 171, 31))
		#Page_Tres
		self.ui.pushButton_NewFaVidComp.setGeometry(QtCore.QRect(190+extender, 130, 400, 41))
		self.ui.pushButton_NewFacCamComp.setGeometry(QtCore.QRect(190+extender, 270, 400, 41))
		#self.ui.bt_menu.clicked.connect(self.mover_menu2)

	def mover_menu(self):
		if True:			
			width = self.ui.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 200
				#Page_Uno
				self.ui.lineEdit.setGeometry(QtCore.QRect(170, 100, 250, 41))
				self.ui.lineEdit_NewProgram.setGeometry(QtCore.QRect(100, 180, 391, 51))
				self.ui.pushButton_NewProg.setGeometry(QtCore.QRect(210, 300, 171, 31))
				#Page_Dos
				self.ui.lineEdit_3.setGeometry(QtCore.QRect(170, 100, 250, 41))
				self.ui.lineEdit_NewMail.setGeometry(QtCore.QRect(100, 190, 391, 51))
				self.ui.pushButton_NewMail.setGeometry(QtCore.QRect(210, 310, 171, 31))
				#Page_Tres
				self.ui.pushButton_NewFaVidComp.setGeometry(QtCore.QRect(90, 130, 400, 41))
				self.ui.pushButton_NewFacCamComp.setGeometry(QtCore.QRect(90, 270, 400, 41))
				
			else:
				extender = normal
				#Page_Uno
				self.ui.lineEdit.setGeometry(QtCore.QRect(250+extender, 100, 250, 41))
				self.ui.lineEdit_NewProgram.setGeometry(QtCore.QRect(180+extender, 180, 391, 51))
				self.ui.pushButton_NewProg.setGeometry(QtCore.QRect(290+extender, 300, 171, 31))
				#Page_Dos
				self.ui.lineEdit_3.setGeometry(QtCore.QRect(250+extender, 100, 250, 41))
				self.ui.lineEdit_NewMail.setGeometry(QtCore.QRect(180+extender, 190, 391, 51))
				self.ui.pushButton_NewMail.setGeometry(QtCore.QRect(290+extender, 310, 171, 31))
				#Page_Tres
				self.ui.pushButton_NewFaVidComp.setGeometry(QtCore.QRect(190+extender, 130, 400, 41))
				self.ui.pushButton_NewFacCamComp.setGeometry(QtCore.QRect(190+extender, 270, 400, 41))
			
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	def mover_menu2(self):
		if True:			
			width = self.ui.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 200
				auxWidth = int((756-self.ui.page_uno.width())/5)+50
				#Page_Uno
				self.ui.lineEdit.setGeometry(QtCore.QRect(250+auxWidth, 100, 250, 41))
				self.ui.lineEdit_NewProgram.setGeometry(QtCore.QRect(180+auxWidth, 180, 391, 51))
				self.ui.pushButton_NewProg.setGeometry(QtCore.QRect(290+auxWidth, 300, 171, 31))
				#Page_Dos
				self.ui.lineEdit_3.setGeometry(QtCore.QRect(250+auxWidth, 100, 250, 41))
				self.ui.lineEdit_NewMail.setGeometry(QtCore.QRect(180+auxWidth, 190, 391, 51))
				self.ui.pushButton_NewMail.setGeometry(QtCore.QRect(290+auxWidth, 310, 171, 31))
				#Page_Tres
				self.ui.pushButton_NewFaVidComp.setGeometry(QtCore.QRect(190+auxWidth, 130, 400, 41))
				self.ui.pushButton_NewFacCamComp.setGeometry(QtCore.QRect(190+auxWidth, 270, 400, 41))
				
			else:
				extender = normal
				#Page_Uno
				self.ui.lineEdit.setGeometry(QtCore.QRect(250+extender, 100, 250, 41))
				self.ui.lineEdit_NewProgram.setGeometry(QtCore.QRect(180+extender, 180, 391, 51))
				self.ui.pushButton_NewProg.setGeometry(QtCore.QRect(290+extender, 300, 171, 31))
				#Page_Dos
				self.ui.lineEdit_3.setGeometry(QtCore.QRect(250+extender, 100, 250, 41))
				self.ui.lineEdit_NewMail.setGeometry(QtCore.QRect(180+extender, 190, 391, 51))
				self.ui.pushButton_NewMail.setGeometry(QtCore.QRect(290+extender, 310, 171, 31))
				#Page_Tres
				self.ui.pushButton_NewFaVidComp.setGeometry(QtCore.QRect(190+extender, 130, 400, 41))
				self.ui.pushButton_NewFacCamComp.setGeometry(QtCore.QRect(190+extender, 270, 400, 41))
			
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	


