from django.contrib import admin
from models import Persona
#Administrador no es necesario
#from models import Administrador
from models import MasterTeacher
from models import HistorialLaboral
from models import HistorialAcademico
from models import Inscrito
from models import LeaderTeacher
from models import AreaFormacion
from models import ActividadEvaluacion
from models import Curso
from models import Cohorte
from models import Calificacion
from models import LeaderTeacher_Cohorte
from models import ZonaInstitucionEducativa
from models import CaracterTecnica
from models import EtniaEducativa
from models import GradosEscolares
from models import NivelEscolar
from models import AreaFormacionDesarrollada



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


#Recarga la lista de curso.


class MasterTeacherAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
    'primer_apellido', 'segundo_apellido','nombre_usuario','identificacion_usuario')
    #busca deacuerdo a la llave foranea
    search_fields = ('persona__identificacion', 'persona__primer_nombre',
        'persona__segundo_nombre', 'persona__primer_apellido',
        'persona__segundo_apellido','user__id')
admin.site.register(MasterTeacher, MasterTeacherAdmin)

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
    'primer_apellido', 'segundo_apellido')
    #criterios de filtro de busqueda
    search_fields = ('persona__identificacion', 'persona__primer_nombre',
        'persona__segundo_nombre', 'persona__primer_apellido',
        'persona__segundo_apellido')

admin.site.register(Inscrito, InscritoAdmin)


class LeaderTeacherAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
    'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 
    'ciudad_nacimiento', 'pais_nacimiento', 'ciudad_residencia',
     'pais_residencia', 'ciudad_labora', 'departamento_labora',
     'fecha_activacion','nombre_usuario','identificacion_usuario')
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
    list_display = ('descripcion', 'peso')
    search_fields = ('descripcion', 'peso')
admin.site.register(ActividadEvaluacion, ActividadEvaluacionAdmin)


#Recarga la lista de curso.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'descripcion')
    search_fields = ('nombre', 'estado')
    filter_horizontal = ('actividad_evaluacion',)
admin.site.register(Curso, CursoAdmin)


#Recarga la lista de cohorte.
class CohorteAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'fecha_fin', 'nombre_curso',
    'id_Master_Teacher', 'nombre_Master_Teacher')
    #busca deacuerdo a la llave foranea
    search_fields = ('fecha_inicio', 'fecha_fin', 'curso__nombre',
    'master_teacher__persona__identificacion',
    'master_teacher__persona__primer_nombre')
admin.site.register(Cohorte, CohorteAdmin)
admin.site.register(Calificacion)
admin.site.register(LeaderTeacher_Cohorte)

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

