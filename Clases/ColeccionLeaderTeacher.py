from Coleccion import Coleccion

class ColeccionLeaderTeacher(Coleccion):
	
	def __init__(self):
		self.coleccion = []

	def add(self,objeto):
		self.coleccion.append(objeto)

	def get(self, indice):
		return self.coleccion.get(indice)

	def remove(self,objeto):
		self.coleccion.remove(objeto)