# SIGECUC-TIC
Sistema de Gestión de Cursos en Competencias TIC es un proyecto para la asignatura desarrollo de sotfware II Universidad del Vlle para el periodo academico FEB-JUN 2015.

## ¿Que es SIGECUC-TIC?

Sistema de Gestión de Cursos en Competencias TIC (SIGECUC-TIC) es una aplicación WEB, que implementa los siguientes procesos:

* **Gestión información de usuarios:**

* **Inicio de sesión y autenticación de usuarios**.

* **Gestión de inscripción de estudiantes en los cursos o asignaturas creadas** Inscribir, modificar y eliminar inscripciones a un curso. El estudiante antes de llevar cabo la inscripción en algún curso, deberá digitar los datos necesarios para la inscripción, los cuales  son: datos personales, demográficos, historial académico, historial laboral. 

* **Envio de correos electrónicos**, el sistema notifica vía correo electrónico a cada estudiante, en qué curso y cohorte quedará ubicado para empezar su formación.

* **Gestión de información de formadores**

* **Gestión de información de cursos de formación:** 

* **Gestión de información de cohortes de cada curso de formación:** Crear, modificar, eliminar registros de cohortes de uno o varios cursos.

* **Gestionar información de notas:** El sistema permite, a los formadores de formadores, registrar, modificar y eliminar notas de las actividades de evaluación de los cursos de los determinados cohortes a que tenga acceso.

* Asigna el tipo de certificado alcanzado por cada docente según la asistencia y el porcentaje de la nota final.

* **Generación de Reportes**

-[x] Cursos con mayor número de asistentes en el mes (Top 10).

-[x] Número de estudiantes que han llegado en el mes de cada departamento de la región.

[x] Curso con menos potencial de avance (5 cursos). Qué criterios se usan para medir el potencial de avance de un grupo.

[x] Porcentaje de estudiantes que aprobaron los cursos de un semestre por departamento.

[x] Porcentaje de estudiantes que reprobaron los cursos de un semestre por departamento. 

[x] Detalle de notas por estudiantes.

[x] Histórico de estudiantes que hayan ganado un curso.

[x] Detalle de estudiantes en un curso por departamentos.

## Requerimientos
python 2.7.3, Django 1.7

#Instalar Django 
sudo apt-get install python-pip
sudo pip install Django==1.7

#Instalar Base de datos postgress
sudo apt-get install postgresql postgresql-contrib

#Instalar el controlador de python para postgres
sudo apt-get install python-psycopg2





