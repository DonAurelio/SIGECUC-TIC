from django.contrib import admin
from models import Persona
#Administrador no es necesario
#from models import Administrador
from models import MasterTeacher
from models import HistorialLaboral
#from models import HistorialAcademico
from models import Inscrito
from models import LeaderTeacher
from models import AreaFormacion
from models import ActividadEvaluacion
from models import Curso
from models import Cohorte
from models import Calificacion
from models import LeaderTeacher_Cohorte


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
admin.site.register(MasterTeacher)
admin.site.register(HistorialLaboral)
admin.site.register(Inscrito)
admin.site.register(LeaderTeacher)
admin.site.register(AreaFormacion)
admin.site.register(ActividadEvaluacion)
admin.site.register(Curso)
admin.site.register(Cohorte)
admin.site.register(Calificacion)
admin.site.register(LeaderTeacher_Cohorte)


