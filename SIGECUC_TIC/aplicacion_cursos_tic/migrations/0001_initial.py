# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEvaluacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('peso', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AreaFormacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota_actividad', models.DecimalField(max_digits=3, decimal_places=2)),
                ('actividad', models.ForeignKey(to='aplicacion_cursos_tic.ActividadEvaluacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(max_length=30)),
                ('actividad_evaluacion', models.ManyToManyField(to='aplicacion_cursos_tic.ActividadEvaluacion')),
                ('area_formacion', models.ManyToManyField(to='aplicacion_cursos_tic.AreaFormacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistorialAcademico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zona_labor_docente', models.CharField(max_length=50)),
                ('caracter_educacion_media', models.CharField(max_length=50)),
                ('etnia_educativa', models.CharField(max_length=50)),
                ('nivel_educativo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistorialLaboral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exp_preescolar', models.CharField(max_length=50)),
                ('exp_primaria', models.CharField(max_length=50)),
                ('exp_secundaria', models.CharField(max_length=50)),
                ('exp_media', models.CharField(max_length=50)),
                ('exp_superior', models.CharField(max_length=50)),
                ('exp_rural', models.CharField(max_length=50)),
                ('exp_urbano', models.CharField(max_length=50)),
                ('exp_publico', models.CharField(max_length=50)),
                ('exp_privado', models.CharField(max_length=50)),
                ('exp_total', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LeaderTeacher_Cohorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota_final', models.DecimalField(max_digits=3, decimal_places=2)),
                ('cohorte', models.ForeignKey(to='aplicacion_cursos_tic.Cohorte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('identificacion', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(default=b'', max_length=30)),
                ('primer_apellido', models.CharField(max_length=40)),
                ('segundo_apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=40)),
                ('estado_civil', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MasterTeacher',
            fields=[
                ('contrasenia', models.CharField(max_length=40)),
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='aplicacion_cursos_tic.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LeaderTeacher',
            fields=[
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='aplicacion_cursos_tic.Persona')),
                ('contrasenia', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('ciudad_nacimiento', models.CharField(max_length=30)),
                ('pais_nacimiento', models.CharField(max_length=30)),
                ('ciudad_residencia', models.CharField(max_length=30)),
                ('pais_residencia', models.CharField(max_length=30)),
                ('ciudad_labora', models.CharField(max_length=30)),
                ('departamento_labora', models.CharField(max_length=30)),
                ('fecha_activacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='aplicacion_cursos_tic.Persona')),
                ('fecha_inscripcion', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
                ('historial_academico', models.OneToOneField(to='aplicacion_cursos_tic.HistorialAcademico')),
                ('historial_laboral', models.OneToOneField(to='aplicacion_cursos_tic.HistorialLaboral')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('contrasenia', models.CharField(max_length=40)),
                ('persona', models.OneToOneField(primary_key=True, serialize=False, to='aplicacion_cursos_tic.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='leaderteacher_cohorte',
            name='leader_teacher',
            field=models.ForeignKey(to='aplicacion_cursos_tic.LeaderTeacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cohorte',
            name='curso',
            field=models.ForeignKey(to='aplicacion_cursos_tic.Curso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cohorte',
            name='master_teacher',
            field=models.ForeignKey(to='aplicacion_cursos_tic.MasterTeacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificacion',
            name='cohorte',
            field=models.ForeignKey(to='aplicacion_cursos_tic.Cohorte'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificacion',
            name='leader_teacher',
            field=models.ForeignKey(to='aplicacion_cursos_tic.LeaderTeacher'),
            preserve_default=True,
        ),
    ]
