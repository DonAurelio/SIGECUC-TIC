"""
Django settings for SIGECUC_TIC project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!y8iw$8(po$u-z$pm9inbf4cn1il81!q8qv65uoe_amow+9@nv'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth', #Menejo de autenticacion y autorizacion de usuarios en el sistema
'django.contrib.contenttypes',
'django.contrib.sessions', #Aplicacion Django para el manejo de seciones
'django.contrib.messages',
'django.contrib.staticfiles',
'aplicacion_cursos_tic', #Aplicacion SIGECUC_TIC
)
MIDDLEWARE_CLASSES = (
'django.contrib.sessions.middleware.SessionMiddleware', #Middleware Django para el inicio de sesion
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware', #Middleware Django para autenticacion de usuarios
'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',

)
ROOT_URLCONF = 'SIGECUC_TIC.urls'
WSGI_APPLICATION = 'SIGECUC_TIC.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# }
#}
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
'NAME': 'sigecuc-ticDB', # Or path to database file if using sqlite3.
'USER': 'sigecuc-tic', # Not used with sqlite3.
'PASSWORD': 'sigecuc-tic', # Not used with sqlite3.
'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
'PORT': '', # Set to empty string for default. Not used with sqlite3.
}
}

#Modificacion paths (Aurelio)
SETTINGS_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(SETTINGS_DIR, 'templates').replace('\\','/')
#Ubicacion de los templates relacionados con las cuentas de los usuarios
TEMPLATE_PATH_ACCOUNTS = os.path.join(SETTINGS_DIR, 'templates/cuentas').replace('\\','/')

#Declaramos la ruta donde quedaran alamcenadas todas las templates del proyecto
TEMPLATE_DIRS = (
TEMPLATE_PATH,
TEMPLATE_PATH_ACCOUNTS,
)
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

#Modificacion paths (Aurelio)
STATIC_PATH = os.path.join(SETTINGS_DIR,'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
