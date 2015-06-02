from django import forms
from django.contrib.auth.models import User
from apps.cursos.models import Persona
from apps.cursos.models import LeaderTeacher

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
	

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona


class LeaderTeacherForm(forms.ModelForm):
	class Meta:
		model = LeaderTeacher