from django.contrib import admin

#Imporando modelos de la aplicacion cursos
from apps.inicio.models import Persona
from apps.inicio.models import MasterTeacher
from apps.inicio.models import LeaderTeacher

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
     'fecha_activacion','nombre_usuario','identificacion_usuario')
"""
    search_fields = ('persona__identificacion', 'persona__primer_nombre',
        'persona__segundo_nombre', 'persona__primer_apellido',
        'persona__segundo_apellido', 'fecha_nacimiento',
          'ciudad_residencia', 'pais_residencia',
         'ciudad_labora', 'departamento_labora', 'fecha_activacion')
"""
admin.site.register(LeaderTeacher, LeaderTeacherAdmin)