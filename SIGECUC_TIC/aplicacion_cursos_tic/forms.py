from django import forms


#Es la clase relacionada con el formulario de login.html
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

