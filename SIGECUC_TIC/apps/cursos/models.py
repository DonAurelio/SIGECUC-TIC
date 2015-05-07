from django.db import models
from apps.inicio.models import Persona
from apps.inicio.models import MasterTeacher
from apps.inicio.models import LeaderTeacher

#====================> HISTORIAL ACADEMICO <====================== 
class ZonaInstitucionEducativa(models.Model):
	zona = models.CharField(max_length=50)
	class Meta:
		ordering = ["zona"]
		verbose_name_plural = "Ver ZonaInstitucionEducativa"

	def __str__(self):
		return '%s' % (self.zona)


class CaracterTecnica(models.Model):
	caracter_tecnico = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Ver CaracterTecnica"

	def __str__(self):
		return '%s' % (self.caracter_tecnico)     


class EtniaEducativa(models.Model):
	etnia_educativa = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Ver EtniaEducativa"

	def __str__(self):
		return '%s' % (self.etnia_educativa)       

class NivelEscolar(models.Model):
	nivel_escolar = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Ver Nivel Escolar"

	def __str__(self):
		return '%s' % (self.nivel_escolar)  

class GradosEscolares(models.Model):
	grado_escolar = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Ver Grados Escolares"

	def __str__(self):
		return '%s' % (self.grado_escolar)  


class AreaFormacionDesarrollada(models.Model):
	area_formacion = models.CharField(max_length=200)
	class Meta:
		ordering = ["area_formacion"]
		verbose_name_plural = "Ver Area Formacion Desarrollada"

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
		verbose_name_plural = "Ver Historiales Academicos"

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
		verbose_name_plural = "Ver Historiales Laborales"

	def __str__(self):
		return '%s' % (self.id)
#====================> FIN HISTORIAL LABORAL <============================ 


#=========================> CURSOS <====================================== 
class AreaFormacion(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	class Meta:
			ordering = ["nombre"]
			verbose_name_plural = "Ver Area de formacion"

	def __str__(self):
		return '%s' % (self.nombre)


class ActividadEvaluacion(models.Model):
	descripcion = models.TextField()
	peso = models.DecimalField(max_digits=3, decimal_places=2)  # ej: 0.75

	class Meta:
		ordering = ["descripcion"]
		verbose_name_plural = "Ver Actividad de evaluacion"

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
		verbose_name_plural = "Ver Cursos"

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
		verbose_name_plural = "Ver Cohortes"
#=========================> FIN COHORTES <============================

#=========================> INSCRITO <================================
class Inscrito(models.Model):
	persona = models.OneToOneField(Persona, primary_key=True)
	fecha_inscripcion = models.DateField(auto_now_add=True)
	estado = models.BooleanField(default=True)
	historial_laboral = models.OneToOneField(HistorialLaboral)  # delete cascade
	historial_academico = models.OneToOneField(HistorialAcademico)
	curso = models.ForeignKey(Curso)

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

#=========================> FIN INSCRITO <=============================

#=========================> CALIFICACION <=============================
class Calificacion(models.Model):
	nota_actividad = models.DecimalField(max_digits=3, decimal_places=2)  # 4.25
	leader_teacher = models.ForeignKey(LeaderTeacher)
	cohorte = models.ForeignKey(Cohorte)
	actividad = models.ForeignKey(ActividadEvaluacion)
#=========================> FIN CALIFICACION <=========================

#=========================> LEADER_TEACHER_COHORTE <===================
class LeaderTeacher_Cohorte(models.Model):
	nota_final = models.DecimalField(max_digits=3, decimal_places=2)
	leader_teacher = models.ForeignKey(LeaderTeacher)
	cohorte = models.ForeignKey(Cohorte)
#=========================> FIN LEADER_TEACHER_COHORTE <===============