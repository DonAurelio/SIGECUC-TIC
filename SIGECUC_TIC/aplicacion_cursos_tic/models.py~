from django.db import models

# Create your models here.

from django.db import models


class Persona(models.Model):
    identificacion = models.CharField(max_length=20, primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, default='')
    primer_apellido = models.CharField(max_length=40)
    segundo_apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=40)
    estado_civil = models.CharField(max_length=20)


class Administrador(models.Model):
    contrasenia = models.CharField(max_length=40)
    persona = models.OneToOneField(Persona, primary_key=True)


class MasterTeacher(models.Model):
    contrasenia = models.CharField(max_length=40)
    persona = models.OneToOneField(Persona, primary_key=True)


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


class HistorialAcademico(models.Model):
    zona_labor_docente = models.CharField(max_length=50)
    caracter_educacion_media = models.CharField(max_length=50)
    etnia_educativa = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=50)


class Inscrito(models.Model):
 	persona = models.OneToOneField(Persona, primary_key=True)
	fecha_inscripcion = models.DateField(auto_now_add=True)
 	estado = models.BooleanField(default=True)
 	historial_laboral = models.OneToOneField(HistorialLaboral)  # delete cascade
 	historial_academico = models.OneToOneField(HistorialAcademico)
	 

class LeaderTeacher(models.Model):
	 persona = models.OneToOneField(Persona, primary_key=True)
	 contrasenia = models.CharField(max_length=40)
	 #permiso = models.
	 #viatico = models.
	 fecha_nacimiento = models.DateField()
	 sexo = models.CharField(max_length=1)  # {M, F}
	 ciudad_nacimiento = models.CharField(max_length=30)
	 pais_nacimiento = models.CharField(max_length=30)
	 ciudad_residencia = models.CharField(max_length=30)
	 pais_residencia = models.CharField(max_length=30)
	 ciudad_labora = models.CharField(max_length=30)
	 departamento_labora = models.CharField(max_length=30)
	 fecha_activacion = models.DateField()


class AreaFormacion(models.Model):
    descripcion = models.TextField()


class ActividadEvaluacion(models.Model):
    descripcion = models.TextField()
    peso = models.DecimalField(max_digits=3, decimal_places=2)  # ej: 0.75


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=30)  # BooleanField?
    area_formacion = models.ManyToManyField(AreaFormacion)
    actividad_evaluacion = models.ManyToManyField(ActividadEvaluacion)


class Cohorte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    curso = models.ForeignKey(Curso)
    master_teacher = models.ForeignKey(MasterTeacher)


class Calificacion(models.Model):
    nota_actividad = models.DecimalField(max_digits=3, decimal_places=2)  # 4.25
    leader_teacher = models.ForeignKey(LeaderTeacher)
    cohorte = models.ForeignKey(Cohorte)
    actividad = models.ForeignKey(ActividadEvaluacion)


class LeaderTeacher_Cohorte(models.Model):
    nota_final = models.DecimalField(max_digits=3, decimal_places=2)
    leader_teacher = models.ForeignKey(LeaderTeacher)
    cohorte = models.ForeignKey(Cohorte)
