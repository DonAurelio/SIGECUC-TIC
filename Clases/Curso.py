class Curso:

    def __init__(self, id_curso, id_area_formacion, nombre, descripcion, estado,
        cohortes, actividadesEvaluacion, areaDeFormacion):
        self.id_curso = id_curso
        self.id_area_formacion = id_area_formacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.cohortes = cohortes
        self.actividadesEvaluacion = actividadesEvaluacion
        self.areaDeFormacion = areaDeFormacion

    def getId_curso(self):
        return self.id_curso

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getEstado(self):
        return self.estado

    def setId_curso(self, id_curso):
        self.id_curso = id_curso

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setEstado(self, estado):
        self.estado = estado



