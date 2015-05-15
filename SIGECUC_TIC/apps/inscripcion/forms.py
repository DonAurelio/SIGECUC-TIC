from django import forms
from apps.cursos.models import Persona
from apps.cursos.models import HistorialLaboral
from apps.cursos.models import HistorialAcademico
from apps.cursos.models import ZonaInstitucionEducativa
from apps.cursos.models import CaracterTecnica
from apps.cursos.models import EtniaEducativa
from apps.cursos.models import GradosEscolares
from apps.cursos.models import NivelEscolar
from apps.cursos.models import AreaFormacionDesarrollada
from apps.cursos.models import Inscrito
from apps.cursos.models import Persona


class InscripcionPersonaForm(forms.ModelForm):
	class Meta:
		model = Persona

class HistorialAcademicoForm(forms.ModelForm):
	zona_institucion_educativa = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		queryset=ZonaInstitucionEducativa.objects.all())
	caracter_tecnica = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		queryset=CaracterTecnica.objects.all())
	etnia_educativa = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		queryset=EtniaEducativa.objects.all())
	grado_escolar = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		queryset=GradosEscolares.objects.all())
	nivel_Escolar = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		queryset=NivelEscolar.objects.all())
	area_formacion_desarrollada = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		queryset=AreaFormacionDesarrollada.objects.all())
	class Meta:
		model = HistorialAcademico

class HistorialLaboralForm(forms.ModelForm):
	class Meta:
		model = HistorialLaboral

class InscripcionConsulaForm(forms.Form):
	identificacion = forms.CharField(label='Numero Identificacion',max_length=11,required=True)	