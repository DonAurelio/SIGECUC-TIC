from django import forms

from .models import Persona

class Informacion_personalForm(forms.ModelForm):
	#Dehabilita un campo en el formulario
	identificacion = forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	primer_nombre = forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	segundo_nombre = forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}),required=False)
	primer_apellido = forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	segundo_apellido = forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	class Meta:
		model = Persona
		exclude = ['estado_civil', 'sexo']




		
