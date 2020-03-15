from email.message import EmailMessage
import smtplib
import acceptcode.functions as functions

class SendYandexEmail():
	def __init__(self, email, password, to):
		self.Email = email
		self.Password = password
		self.message = functions.GenerateSecretKey()
		self.To = to

		self.msg = EmailMessage()

		self.msg['Subject'] = 'Your secret code'
		self.msg['From'] = self.Email
		self.msg['To'] = self.To

	def send(self):
		self.msg.set_content(self.message)

		with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as smtp:
			smtp.login(self.Email,self.Password)
			smtp.send_message(self.msg)	

