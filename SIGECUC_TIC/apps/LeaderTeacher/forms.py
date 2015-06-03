from django import forms

from apps.cursos.models import LeaderTeacher

class LeaderTeacherForm(forms.ModelForm):
	class Meta:
		model = LeaderTeacher
		exclude = ['user', 'inscrito','dia','mes','anio','cohorte']