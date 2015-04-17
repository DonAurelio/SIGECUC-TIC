from django import forms 

#Clas LoginForm
#Es la clase relacionada con el formulario de login.html
class LoginForm(forms.Form):
	nombre_usuario = forms.CharField()
	contrasenia = forms.CharField(widget=forms.PasswordInput())

