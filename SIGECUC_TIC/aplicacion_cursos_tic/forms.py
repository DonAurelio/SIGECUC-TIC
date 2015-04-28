from django import forms
from aplicacion_cursos_tic.models import Inscrito

#Clas LoginForm
#Es la clase relacionada con el formulario de login.html
class LoginForm(forms.Form):
	nombre_usuario = forms.CharField()
	contrasenia = forms.CharField(widget=forms.PasswordInput())


class addInscripcionForm(forms.ModelForm):
	class Meta:
		model = Inscrito
		exclude = {'estado',}


