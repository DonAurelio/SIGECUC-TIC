class Cohorte:

    def __init__(self, id_cohorte, nombre, descripcion, fechaInicio, fechaFin,
        MasterTeacher):
        self.id_cohorte = id_cohorte
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.MasterTeacher = MasterTeacher

    def getId_cohorte(self):
        return self.id_cohorte

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getFechaInicio(self):
        return self.fechaInicio

    def getFechaFin(self):
        return self.fechaFin

    def setId_cohorte(self, id_cohorte):
        self.id_cohorte = id_cohorte

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setFechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio

    def setFechaFin(self, fechaFin):
        self.fechaFin = fechaFin


