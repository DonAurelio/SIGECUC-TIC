import datetime

class TraductorFecha:
	def __init__(self,fecha):

		self.meses = {
		1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",
		7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre",}

		self.mes = fecha.now().month
		self.dia = fecha.now().day
		self.anio = fecha.now().year

	def mes(self):
		return self.meses[self.mes]

	def dia(self):
		return self.dia

	def anio(self):
		return self.anio
		





