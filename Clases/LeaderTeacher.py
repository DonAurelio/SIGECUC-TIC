from Inscrito import Inscrito


class LeaderTeacher(Inscrito):
    def __init__(self, identificacion, nombres, apellidos, email, telefono,
    direccion, estado_civil, fecha_inscripcion, estado, historialAcademico,
     historialLaboral, areaDeFormacion, contrasenia, permiso, viaticos, edad,
     sexo, ciudad_nac, pais_nac, ciudad_rec, departamento_rec, ciudad_labora,
     departamento_labora, calificaciones, NotasFinales, fecha_activacion):
        # llamamos al constructor de Inscrito
        Inscrito.__init__(self, identificacion, nombres, apellidos, email,
        telefono, direccion, estado_civil, fecha_inscripcion, estado,
        historialAcademico, historialLaboral, areaDeFormacion)
        self.contrasenia = contrasenia
        self.permiso = permiso
        self.viaticos = viaticos
        self.edad = edad
        self.sexo = sexo
        self.ciudad_nac = ciudad_nac
        self.pais_nac = pais_nac
        self.ciudad_rec = ciudad_rec
        self.departamento_rec = departamento_rec
        self.ciudad_labora = ciudad_labora
        self.departamento_labora = departamento_labora
        self.calificaciones = calificaciones
        self.notasFinales = NotasFinales
        self.fecha_activacion = fecha_activacion

    def getContrasenia(self):
        return self.contrasenia

    def getPermiso(self):
        return self.permiso

    def getViaticos(self):
        return self.viaticos

    def getEdad(self):
        return self.edad

    def getSexo(self):
        return self.sexo

    def getCiudad_nac(self):
        return self.ciudad_nac

    def getPais_nac(self):
        return self.pais_nac

    def getCiudadRec(self):
        return self.ciudad_rec

    def getDepartamento_rec(self):
        return self.departamento_rec

    def getCiudadLabora(self):
        return self.ciudad_labora

    def getDepartamentoLabora(self):
        return self.departamento_labora

    def getFecha_acitivacion(self):
        return self.fecha_activacion

    def setContrasenia(self, contrasenia):
        self.contrasenia = contrasenia

    def setPermiso(self, permiso):
        self.permiso = permiso

    def setViaticos(self, viaticos):
        self.viaticos = viaticos

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo

    def setCiudad_nac(self, ciudad_nac):
        self.ciudad_nac = ciudad_nac

    def setPais_nac(self, pais_nac):
        self.pais_nac = pais_nac

    def setCiudad_rec(self, ciudad_rec):
        self.ciudad_rec = ciudad_rec

    def setDepartamento_rec(self, departamento_rec):
        self.departamento_rec = departamento_rec

    def setCiudad_labora(self, ciudad_labora):
        self.ciudad_labora = ciudad_labora

    def setDepartamento_labora(self, departamento_labora):
        self.departamento_labora = departamento_labora

    def setFecha_activacion(self, fecha_activacion):
        self.fecha_activacion = fecha_activacion









