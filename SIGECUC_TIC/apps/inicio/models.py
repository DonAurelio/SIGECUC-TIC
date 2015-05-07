from django.db import models
from django.contrib.auth.models import User

#Importamos modelos de la aplicacion cursos

class Persona(models.Model):
	identificacion = models.CharField(max_length=20, primary_key=True)
	primer_nombre = models.CharField(max_length=30)
	segundo_nombre = models.CharField(max_length=30, default='', blank=True)
	primer_apellido = models.CharField(max_length=40)
	segundo_apellido = models.CharField(max_length=40)
	email = models.EmailField(blank=True)
	telefono = models.CharField(max_length=15)
	direccion = models.CharField(max_length=40)
	SOLTERO = 'soltero'
	CASADO = 'casado'
	VIUDO = 'viudo'
	#Se define una lista desplegable
	estado = (
		(SOLTERO, 'Soltero'),
		(CASADO, 'Casado'),
		(VIUDO, 'Viudo'),
	)
	estado_civil = models.CharField(max_length=20, choices=estado,
	default=SOLTERO)

	MASCULINO = 'MASCULINO'
	FEMENINO = 'FEMENINO'
	tipo_sexo = (
		(MASCULINO,'MASCULINO'),
		(FEMENINO, 'FEMENINO'),

	)
	#Falta definir el sexo en el modelo
	sexo = models.CharField(max_length=20, choices=tipo_sexo,
	default=MASCULINO)

	class Meta:
			ordering = ["primer_nombre"]
			verbose_name_plural = "Ver Personas"

	def __str__(self):
		return '%s %s %s %s %s' % (self.identificacion,
		self.primer_nombre, self.segundo_nombre, self.primer_apellido,
		self.segundo_apellido)






# Create your models here.
class MasterTeacher(models.Model):
	persona = models.OneToOneField(Persona, primary_key=True)
	user = models.ForeignKey(User,unique=True)
	
	#metodo para que retorne la identificacion de persona
	def identificacion(self):
		return (self.persona.identificacion)

	#metodo para que retorne el primer_nombre de persona
	def primer_nombre(self):
		return (self.persona.primer_nombre)

	#metodo para que retorne el segundo_nombre de  persona
	def segundo_nombre(self):
		return (self.persona.segundo_nombre)

	#metodo para que retorne el primer_apellido de  persona
	def primer_apellido(self):
		return (self.persona.primer_apellido)

	#metodo para que retorne el segundo_apellido de  persona
	def segundo_apellido(self):
		return (self.persona.segundo_apellido)

	def nombre_usuario(self):
		return (self.user.username)

	def identificacion_usuario(self):
		return (self.user.id)

	class Meta:
		verbose_name_plural = "Ver Master Teacher"

	def __str__(self):
		return '%s %s %s' % (self.persona.identificacion,
			 self.persona.primer_nombre, self.persona.primer_apellido)


class LeaderTeacher(models.Model):
	#inscrito = models.OneToOneField(Inscrito, primary_key=True)
	user = models.ForeignKey(User,unique=True)
	#permiso = models.
	#viatico = models.

	#metodo para que retorne la identificacion de persona
	def identificacion(self):
		return (self.inscrito.persona.identificacion)

	#metodo para que retorne el primer_nombre de persona
	def primer_nombre(self):
		return (self.inscrito.persona.primer_nombre)

	#metodo para que retorne el segundo_nombre de  persona
	def segundo_nombre(self):
		return (self.inscrito.persona.segundo_nombre)

	#metodo para que retorne el primer_apellido de  persona
	def primer_apellido(self):
		return (self.inscrito.persona.primer_apellido)

	#metodo para que retorne el segundo_apellido de  persona
	def segundo_apellido(self):
		return (self.inscrito.persona.segundo_apellido)

	def nombre_usuario(self):
		return (self.user.username)

	def identificacion_usuario(self):
		return (self.user.id)
	
	#Se define una lista desplegable
	fecha_nacimiento = models.DateField()
	ciudad_nacimiento = models.CharField(max_length=30)
	pais_nacimiento = models.CharField(max_length=30)
	ciudad_residencia = models.CharField(max_length=30)
	pais_residencia = models.CharField(max_length=30)
	ciudad_labora = models.CharField(max_length=30)
	departamento_labora = models.CharField(max_length=30)
	fecha_activacion = models.DateField()

	class Meta:
		verbose_name_plural = "Ver Leader Teacher"


