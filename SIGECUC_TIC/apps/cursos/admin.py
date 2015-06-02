from django.contrib import admin
from apps.cursos.models import *


#Recarga la lista de persona y se podra ver tres columnas Nombres,y E-mail.
class PersonaAdmin(admin.ModelAdmin):
	list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
		 'primer_apellido', 'segundo_apellido')
	search_fields = ('identificacion', 'primer_nombre', 'segundo_nombre',
		 'primer_apellido', 'segundo_apellido')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(Persona, PersonaAdmin)
#Administrador no es necesario
#admin.site.register(Administrador)

# Register your models here.
class MasterTeacherAdmin(admin.ModelAdmin):
	list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
	'primer_apellido', 'segundo_apellido','nombre_usuario','identificacion_usuario')
	#busca deacuerdo a la llave foranea
	search_fields = ('persona__identificacion', 'persona__primer_nombre',
		'persona__segundo_nombre', 'persona__primer_apellido',
		'persona__segundo_apellido','user__id')
admin.site.register(MasterTeacher, MasterTeacherAdmin)

class LeaderTeacherAdmin(admin.ModelAdmin):
	list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
	'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 
	'ciudad_nacimiento', 'pais_nacimiento', 'ciudad_residencia',
	 'pais_residencia', 'ciudad_labora', 'departamento_labora',
	 'dia','mes','anio','nombre_usuario','identificacion_usuario')
"""
	search_fields = ('persona__identificacion', 'persona__primer_nombre',
		'persona__segundo_nombre', 'persona__primer_apellido',
		'persona__segundo_apellido', 'fecha_nacimiento',
		  'ciudad_residencia', 'pais_residencia',
		 'ciudad_labora', 'departamento_labora', 'fecha_activacion')
"""
admin.site.register(LeaderTeacher, LeaderTeacherAdmin)

#Recarga la lista de Area_formacion.
class Area_formacionAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')
	search_fields = ('nombre', 'descripcion')
admin.site.register(AreaFormacion, Area_formacionAdmin)


#Recarga la lista de curso.
class ActividadEvaluacionAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion', 'peso')
	search_fields = ('nombre','descripcion', 'peso')
admin.site.register(ActividadEvaluacion, ActividadEvaluacionAdmin)


#Recarga la lista de curso.
class CursoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'estado', 'descripcion')
	search_fields = ('nombre', 'estado')
	filter_horizontal = ('actividad_evaluacion',)
admin.site.register(Curso, CursoAdmin)


#Recarga la lista de cohorte.
class CohorteAdmin(admin.ModelAdmin):
	list_display = ('id','fecha_inicio', 'fecha_fin', 'nombre_curso',
	'id_Master_Teacher', 'nombre_Master_Teacher')
	#busca deacuerdo a la llave foranea
	search_fields = ('fecha_inicio', 'fecha_fin', 'curso__nombre',
	'master_teacher__persona__identificacion',
	'master_teacher__persona__primer_nombre')
admin.site.register(Cohorte, CohorteAdmin)


class CalificacionAdmin(admin.ModelAdmin):
	list_display = ('cohorte','nombre_curso','nombre_actividad','nota_actividad','identificacion_leader_teacher', 
		'primer_nombre_leader_teacher', 'segundo_nombre_leader_teacher','primer_apellido_leader_teacher', 
		'segundo_apellido_leader_teacher')
	search_fields = ('cohorte__curso__nombre', 'nota_actividad', 'actividad__descripcion')

admin.site.register(Calificacion, CalificacionAdmin)


class HistorialLaboralAdmin(admin.ModelAdmin):
	list_display=('id', 'exp_preescolar', 'exp_primaria', 'exp_total')
	search_fields =('id','exp_total')

admin.site.register(HistorialLaboral, HistorialLaboralAdmin)

class HistorialAcademicoAdmin(admin.ModelAdmin):
	list_display=('id', 'caracter_educacion_media')
	search_fields =('id', 'caracter_educacion_media')
admin.site.register(HistorialAcademico, HistorialAcademicoAdmin)

class InscritoAdmin(admin.ModelAdmin):
	#Muestra las columnas de la tabla
	list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
	'primer_apellido', 'segundo_apellido','dia','mes','anio')
	#criterios de filtro de busqueda
	search_fields = ('persona__identificacion', 'persona__primer_nombre',
		'persona__segundo_nombre', 'persona__primer_apellido',
		'persona__segundo_apellido')

admin.site.register(Inscrito, InscritoAdmin)


#Recarga la lista de Area_formacion.
class ZonaInstitucionEducativaAdmin(admin.ModelAdmin):
	list_display = ('id', 'zona')

admin.site.register(ZonaInstitucionEducativa, ZonaInstitucionEducativaAdmin)

class CaracterTecnicaAdmin(admin.ModelAdmin):
	list_display = ('id', 'caracter_tecnico')
admin.site.register(CaracterTecnica, CaracterTecnicaAdmin)

class EtniaEducativaAdmin(admin.ModelAdmin):
	list_display = ('id', 'etnia_educativa')
admin.site.register(EtniaEducativa, EtniaEducativaAdmin)

class GradosEscolaresAdmin(admin.ModelAdmin):
	list_display = ('id', 'grado_escolar')
admin.site.register(GradosEscolares, GradosEscolaresAdmin)

class NivelEscolarAdmin(admin.ModelAdmin):
	list_display = ('id', 'nivel_escolar')
admin.site.register(NivelEscolar, NivelEscolarAdmin)

class AreaFormacionDesarrolladaAdmin(admin.ModelAdmin):
	list_display = ('id', 'area_formacion')
admin.site.register(AreaFormacionDesarrollada, AreaFormacionDesarrolladaAdmin)


class Cursos_InscritoAdmin(admin.ModelAdmin):
    #Muestra las columnas de la tabla
    list_display = ('nombre_curso', 'fecha_inscripcion','identificacion_inscrito', 'primer_nombre_inscrito',
    'segundo_nombre_inscrito', 'primer_apellido_inscrito', 'segundo_apellido_inscrito', 'email_inscrito', 'estado')
    #criterios de filtro de busqueda
    search_fields = ('inscrito__persona__identificacion', 'inscrito__persona__primer_nombre',
        'inscrito__persona__segundo_nombre', 'inscrito__persona__primer_apellido',
        'inscrito__persona__segundo_apellido', 'estado')

admin.site.register(Cursos_Inscrito, Cursos_InscritoAdmin)


class AsistenciaAdmin(admin.ModelAdmin):
    #Muestra las columnas de la tabla
    list_display = ('leader_teacher_identificacion', 'cohorte','dia','mes','anio')
    #criterios de filtro de busqueda
    search_fields = ('leader_teacher__inscrito__persona__identificacion', 'cohorte__curso__nombre')

admin.site.register(Asistencia,AsistenciaAdmin)



