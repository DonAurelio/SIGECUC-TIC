# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUser',
            fields=[
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='cursos.Persona')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
