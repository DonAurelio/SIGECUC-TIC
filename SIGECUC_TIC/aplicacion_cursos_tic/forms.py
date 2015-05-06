from django import forms
from aplicacion_cursos_tic.models import Persona
from aplicacion_cursos_tic.models import HistorialLaboral
from aplicacion_cursos_tic.models import HistorialAcademico
from aplicacion_cursos_tic.models import ZonaInstitucionEducativa
from aplicacion_cursos_tic.models import CaracterTecnica
from aplicacion_cursos_tic.models import EtniaEducativa
from aplicacion_cursos_tic.models import GradosEscolares
from aplicacion_cursos_tic.models import Inscrito
from aplicacion_cursos_tic.models import Persona


#Clas LoginForm
#Es la clase relacionada con el formulario de login.html
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())


class InscripcionPersonaForm(forms.ModelForm):
	class Meta:
		model = Persona

class HistorialAcademicoForm(forms.ModelForm):
	#zona_institucion_educativa = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=ZonaInstitucionEducativa.objects.all())
	#caracter_tecnica = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=CaracterTecnica.objects.all())
	#etnia_educativa = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=EtniaEducativa.objects.all())
	#grado_escolar = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=GradosEscolares.objects.all())
	class Meta:
		model = HistorialAcademico

class HistorialLaboralForm(forms.ModelForm):
	class Meta:
		model = HistorialLaboral


class Persona_MasterTeacherForm(forms.ModelForm):
	class Meta:
		model = Persona




		
