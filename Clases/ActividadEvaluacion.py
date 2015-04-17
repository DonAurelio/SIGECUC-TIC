class ActividadEvaluacion:

    def __init__(self, id_actividad, descripcion, peso):
        self.id_actividad = id_actividad
        self.descripcion = descripcion
        self.peso = peso

    def getId_actividad(self):
        return self.id_actividad

    def getDescripcion(self):
        return self.descripcion

    def getPeso(self):
        return self.peso

    def setId_actividad(self, id_actividad):
        self.id_actividad = id_actividad

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setPeso(self, peso):
        self.peso = peso



