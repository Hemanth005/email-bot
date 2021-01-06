import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'hemanth rao'
email['to'] = 'tejdeep20012013@gmail.com'
email['subject'] = 'Hi i am just a robot created by hemanth'
email.set_content('Just testing things out...on your demand...HAPPY BIRTHDAY')

with  smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('raohemanth316@gmail.com', 'No password@123')
	smtp.send_message(email)
	print("All done!!!")