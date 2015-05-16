from django.db import models
from django.contrib.auth.models import User
from apps.cursos.models import Persona

# Create your models here.
class RegistroUser(models.Model):
	user = models.ForeignKey(User,unique=True)
	persona = models.OneToOneField(Persona, primary_key=True)
