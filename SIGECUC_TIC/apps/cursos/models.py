from django.db import models
from django.contrib.auth.models import User


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
			verbose_name_plural = "Personas"

	def __str__(self):
		return '%s %s %s %s %s' % (self.identificacion,
		self.primer_nombre, self.segundo_nombre, self.primer_apellido,
		self.segundo_apellido)

# Create your models here.
class MasterTeacher(models.Model):
	user = models.ForeignKey(User,unique=True)
	persona = models.OneToOneField(Persona, primary_key=True)
	
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
		verbose_name_plural = "Master Teacher"

	def __str__(self):
		return '%s %s %s' % (self.persona.identificacion,
			 self.persona.primer_nombre, self.persona.primer_apellido)



#=========================> CURSOS <====================================== 
class AreaFormacion(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	class Meta:
			ordering = ["nombre"]
			verbose_name_plural = "Area de formacion"

	def __str__(self):
		return '%s' % (self.nombre)


class ActividadEvaluacion(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	peso = models.DecimalField(max_digits=3, decimal_places=2)  # ej: 0.75

	class Meta:
		ordering = ["descripcion"]
		verbose_name_plural = "Actividad de evaluacion"

	def __str__(self):
		return '%s' % (self.descripcion)


class Curso(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	ACTIVO = '1'
	INACTIVO = '0'
	estado_curso = (
		(ACTIVO, 'Activo'),
		(INACTIVO, 'Inactivo'),
	)
	estado = models.CharField(max_length=30, choices=estado_curso,
	default=estado_curso)  # BooleanField?
	area_formacion = models.ManyToManyField(AreaFormacion)
	actividad_evaluacion = models.ManyToManyField(ActividadEvaluacion)

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Cursos"

	def __str__(self):
		return '%s' % (self.nombre)
#=========================> FIN CURSOS <============================== 

#=========================> COHORTES <================================
class Cohorte(models.Model):
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	curso = models.ForeignKey(Curso)
	master_teacher = models.ForeignKey(MasterTeacher)

	#metodo para que retorne el nombre del curso
	def nombre_curso(self):
		return (self.curso.nombre)
	master_teacher = models.ForeignKey(MasterTeacher)

	#metodo para que retorne el id del Master Teacher
	def id_Master_Teacher(self):
		return (self.master_teacher.persona.identificacion)

	#metodo para que retorne el nombre del Master Teacher
	def nombre_Master_Teacher(self):
		return '%s %s' % (self.master_teacher.persona.primer_nombre,
			self.master_teacher.persona.primer_apellido)

	class Meta:
		verbose_name_plural = "Cohortes"

	def __str__(self):
		return 'Cohorte: %s Nombre curso: %s %s %s' % (self.id , self.curso.nombre, str(self.fecha_inicio), str(self.fecha_fin))
#=========================> FIN COHORTES <============================


#====================> HISTORIAL ACADEMICO <====================== 
class ZonaInstitucionEducativa(models.Model):
	zona = models.CharField(max_length=50)
	class Meta:
		ordering = ["zona"]
		verbose_name_plural = "ZonaInstitucionEducativa"

	def __str__(self):
		return '%s' % (self.zona)

class CaracterTecnica(models.Model):
	caracter_tecnico = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "CaracterTecnica"

	def __str__(self):
		return '%s' % (self.caracter_tecnico)     

class EtniaEducativa(models.Model):
	etnia_educativa = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "EtniaEducativa"

	def __str__(self):
		return '%s' % (self.etnia_educativa)       

class NivelEscolar(models.Model):
	nivel_escolar = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Nivel Escolar"

	def __str__(self):
		return '%s' % (self.nivel_escolar)  

class GradosEscolares(models.Model):
	grado_escolar = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Grados Escolares"

	def __str__(self):
		return '%s' % (self.grado_escolar)  


class AreaFormacionDesarrollada(models.Model):
	area_formacion = models.CharField(max_length=200)
	class Meta:
		ordering = ["area_formacion"]
		verbose_name_plural = "Area Formacion Desarrollada"

	def __str__(self):
		return '%s' % (self.area_formacion) 

	
class HistorialAcademico(models.Model):
	
	ACADEMICA = 'ACADEMICA'
	TECNICA = 'TECNICA'
	tipo_caracter_educacion = (
	(ACADEMICA,'ACADEMICA'),
	(TECNICA,'TECNICA'),

	)

	caracter_educacion_media = models.CharField(max_length=50,choices=tipo_caracter_educacion)

	NIVEL_TECNICO_PROFECIONAL = 'Nivel Tecnico Profecional'
	NIVEL_TECNOLOGICO = 'Nivel Tecnologico'
	NIVEL_PROFESIONAL = 'Nivel Profesional'
	NORMALISTA_SUPERIOR = 'Normalista Superior'
	LICENCIATURA = 'Licenciatura'
	ESPECIALIZACIONES = 'Especializaciones '
	MAESTRIAS = 'Maestrias'
	DOCTORADOS = 'Doctorados'

	TECNICA = 'TECNICA'
	tipo_nivel_maximo_educacion = (
	(NIVEL_TECNICO_PROFECIONAL,'Nivel Tecnico Profecional'),
	(NIVEL_TECNOLOGICO,'Nivel Tecnologico'),
	(NIVEL_PROFESIONAL,'Nivel Profesional'),
	(NORMALISTA_SUPERIOR,'Normalista Superior'),
	(LICENCIATURA,'Licenciatura'),
	(ESPECIALIZACIONES,'Especializaciones'),
	(MAESTRIAS,'Maestrias'),
	(DOCTORADOS,'Doctorados'),

	)

	nivel_maximo_educacion = models.CharField(max_length=50,choices=tipo_nivel_maximo_educacion)
	zona_institucion_educativa = models.ManyToManyField(ZonaInstitucionEducativa)
	caracter_tecnica = models.ManyToManyField(CaracterTecnica)
	etnia_educativa = models.ManyToManyField(EtniaEducativa)
	grado_escolar = models.ManyToManyField(GradosEscolares)
	nivel_Escolar = models.ManyToManyField(NivelEscolar)
	area_formacion_desarrollada = models.ManyToManyField(AreaFormacionDesarrollada)

	class Meta:
		verbose_name_plural = "Historiales Academicos"

	def __str__(self):
		return '%s' % (self.id)

#====================> FIN HISTORIAL ACADEMICO <======================


#====================> HISTORIAL LABORAL <============================ 
class HistorialLaboral(models.Model):
	exp_preescolar = models.CharField(max_length=50)
	exp_primaria = models.CharField(max_length=50)
	exp_secundaria = models.CharField(max_length=50)
	exp_media = models.CharField(max_length=50)
	exp_superior = models.CharField(max_length=50)
	exp_rural = models.CharField(max_length=50)
	exp_urbano = models.CharField(max_length=50)
	exp_publico = models.CharField(max_length=50)
	exp_privado = models.CharField(max_length=50)
	exp_total = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Historiales Laborales"

	def __str__(self):
		return '%s' % (self.id)
#====================> FIN HISTORIAL LABORAL <============================ 


#=========================> INSCRITO <================================
class Inscrito(models.Model):
	persona = models.OneToOneField(Persona, primary_key=True)
	dia = models.CharField(max_length=2)
	mes = models.CharField(max_length=20)
	anio = models.CharField(max_length=4)
	estado = models.BooleanField(default=True)
	historial_laboral = models.OneToOneField(HistorialLaboral)  # delete cascade
	historial_academico = models.OneToOneField(HistorialAcademico)
	#curso = models.ForeignKey(Curso)

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

	def __str__(self):
		return '%s %s %s %s' % (self.persona.identificacion, self.persona.primer_nombre, 
			self.persona.primer_apellido, self.persona.segundo_apellido) 


class Cursos_Inscrito(models.Model):
	curso = models.ForeignKey(Curso)
	inscrito = models.ForeignKey(Inscrito)
	fecha_inscripcion = models.DateField(auto_now_add=True)

	estado_incripcion_cuso = (
		('Pendiente','Pendiente'),
		('Aceptado','Aceptado')
		)

	estado = models.CharField(choices=estado_incripcion_cuso,max_length=20)

	#retorna el nombre del curso
	def nombre_curso(self):
		return (self.curso.nombre)

	def identificacion_inscrito(self):
		return (self.inscrito.persona.identificacion)

	#metodo para que retorne el primer_nombre de inscrito
	def primer_nombre_inscrito(self):
		return (self.inscrito.persona.primer_nombre)

	#metodo para que retorne el segundo_nombre de inscrito
	def segundo_nombre_inscrito(self):
		return (self.inscrito.persona.segundo_nombre)

	#metodo para que retorne el primer_apellido de inscrito
	def primer_apellido_inscrito(self):
		return (self.inscrito.persona.primer_apellido)

	#metodo para que retorne el segundo_apellido de  inscrito
	def segundo_apellido_inscrito(self):
		return (self.inscrito.persona.segundo_apellido)

	#metodo para que retorne el email de  inscrito
	def email_inscrito(self):
		return (self.inscrito.persona.email)

	class Meta:
		verbose_name_plural = "Cursos de los inscritos"

#=========================> FIN INSCRITO <=============================
class LeaderTeacher(models.Model):
	user = models.ForeignKey(User,unique=True)
	inscrito = models.OneToOneField(Inscrito, primary_key=True)

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
	dia = models.CharField(max_length=2)
	meses = (
	('Enero','Enero'),
	('Febrero','Febrero'),
	('Marzo','Marzo'),
	('Abril','Abril'),
	('Mayo','Mayo'),
	('Junio','Junio'),
	('Julio','Julio'),
	('Agosto','Agosto'),
	('Septiembre','Septiembre'),
	('Octubre','Octubre'),
	('Noviembre','Noviembre'),
	('Diciembre','Diciembre'),
	)
	mes = models.CharField(choices=meses,max_length=20)
	anio = models.CharField(max_length=4)
	cohorte = models.ManyToManyField(Cohorte)

	class Meta:
		verbose_name_plural = "Leader Teacher"

	def __str__(self):
		return '%s %s %s %s' % (self.inscrito.persona.identificacion,
		 self.inscrito.persona.primer_nombre, self.inscrito.persona.primer_apellido,
		 self.inscrito.persona.segundo_apellido )


#=========================> CALIFICACION <=============================
class Calificacion(models.Model):
	#nota_actividad = models.DecimalField(max_digits=3, decimal_places=2)  # 4.25
	nota_actividad = models.CharField(max_length=3, blank=True) #cambio por cadena generaba conflictos
	leader_teacher = models.ForeignKey(LeaderTeacher)
	cohorte = models.ForeignKey(Cohorte)
	actividad = models.ForeignKey(ActividadEvaluacion)

	def identificacion_leader_teacher(self):
		return (self.leader_teacher.inscrito.persona.identificacion)
		#metodo para que retorne el primer_nombre de persona
	def primer_nombre_leader_teacher(self):
		return (self.leader_teacher.inscrito.persona.primer_nombre)

	#metodo para que retorne el segundo_nombre de  persona
	def segundo_nombre_leader_teacher(self):
		return (self.leader_teacher.inscrito.persona.segundo_nombre)

	#metodo para que retorne el primer_apellido de  persona
	def primer_apellido_leader_teacher(self):
		return (self.leader_teacher.inscrito.persona.primer_apellido)

	#metodo para que retorne el segundo_apellido de  persona
	def segundo_apellido_leader_teacher(self):
		return (self.leader_teacher.inscrito.persona.segundo_apellido)

	def nombre_curso(self):
		return(self.cohorte.curso.nombre)

		#metodo para que retorne el segundo_apellido de  persona
	def nombre_actividad(self):
		return (self.actividad.descripcion)

	class Meta:
		verbose_name_plural = "Calificaciones"

#=========================> FIN CALIFICACION <=========================


#========================> ASISTENCIA <==================================
class Asistencia(models.Model):

	meses = (
	('Enero','Enero'),
	('Febrero','Febrero'),
	('Marzo','Marzo'),
	('Abril','Abril'),
	('Mayo','Mayo'),
	('Junio','Junio'),
	('Julio','Julio'),
	('Agosto','Agosto'),
	('Septiembre','Septiembre'),
	('Octubre','Octubre'),
	('Noviembre','Noviembre'),
	('Diciembre','Diciembre'),
	)
	leader_teacher = models.ForeignKey(LeaderTeacher)
	cohorte = models.ForeignKey(Cohorte)
	dia = models.CharField(max_length=2)
	mes = models.CharField(max_length=20,choices=meses)
	anio = models.CharField(max_length=4)
	def leader_teacher_identificacion(self):
		return (self.leader_teacher.inscrito.persona.identificacion)

	class Meta:
		verbose_name_plural = "Asistencias"
	
#========================> FIN ASISTENCIA <==============================


