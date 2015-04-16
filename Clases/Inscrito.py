from Persona import Persona


class Inscrito(Persona):
    def __init__(self, identificacion, nombres, apellidos, email, telefono,
    direccion, estado_civil, fecha_inscripcion, estado, historialAcademico,
     historialLaboral, areaDeFormacion):
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombres, apellidos, email,
             telefono, direccion, estado_civil)
        self.estado_civil = estado_civil
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado
        self.historialAcademico = historialAcademico
        self.historialLaboral = historialLaboral
        #El area de formacion es un array de String
        self.areaDeFormacion = areaDeFormacion

    def getFecha_inscripcion(self):
        return self.fecha_inscripcion

    def getEstado(self):
        return self.estado

    def setFecha_inscripcion(self, fecha_inscripcion):
        self.fecha_inscripcion = fecha_inscripcion




