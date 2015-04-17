class Persona:

    def __init__(self, identificacion, nombres, apellidos, email, telefono,
    direccion, estado_civil):
        self.identificacion = identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.estado_civil = estado_civil

    def getIdentificacion(self):
        return self.identificacion

    def getNombres(self):
        return self.nombres

    def getApellidos(self):
        return self.apellidos

    def getEmail(self):
        return self.email

    def getTelefono(self):
        return self.telefono

    def getDireccion(self):
        return self.direccion

    def getEstado_civil(self):
        return self.estado_civil

    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion

    def setNombres(self, nombres):
        self.nombres = nombres

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setEmail(self, email):
        self.email = email

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setEstado_civil(self, estado_civil):
        self.estado_civil = estado_civil



