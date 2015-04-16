from Persona import Persona


class Administrador(Persona):
    def __init__(self, identificacion, nombres, apellidos, email, telefono,
    direccion, estado_civil, contrasenia):
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombres, apellidos, email,
             telefono, direccion, estado_civil)
        # agregamos el nuevo atributo
        self.contrasenia = contrasenia

    def getContrasenia(self):
        return self.contrasenia

    def setContrasenia(self, contrasenia):
        self.contrasenia = contrasenia




