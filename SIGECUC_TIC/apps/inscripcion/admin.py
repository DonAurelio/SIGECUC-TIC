from django.contrib import admin

# Register your models here.
from .models import Inscrito
from .models import HistorialLaboral
from .models import HistorialAcademico
from .models import ZonaInstitucionEducativa
from .models import CaracterTecnica
from .models import EtniaEducativa
from .models import GradosEscolares
from .models import NivelEscolar
from .models import AreaFormacionDesarrollada

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

