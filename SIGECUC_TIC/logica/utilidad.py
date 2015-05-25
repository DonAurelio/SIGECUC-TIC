import datetime
from django.core.mail import EmailMultiAlternatives

class TraductorFecha:
	def __init__(self,fecha):

		self.meses = {
		1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",
		7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre",}

		self.mes = fecha.now().month
		self.dia = fecha.now().day
		self.anio = fecha.now().year

	def get_mes(self):
		return self.meses[self.mes]

	def get_dia(self):
		return self.dia

	def get_anio(self):
		return self.anio


class EmailSender:

	def __init__(self,email,nombre_curso):
		subject = 'Asunto'
		text_content = 'Mensaje...nLinea 2nLinea3'
		html_content = '<h2>Notificacion registro</h2><p>La inscripcion al curso</p>'
		html_content += nombre_curso 
		html_content += '<p>se ha realizado con exito, se informara a traves de este medio su aprobacion</p>'
		from_email = '"SIGECUC-TIC" <emisor.telnet.univalle@gmail.com>'
		to = email
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		





