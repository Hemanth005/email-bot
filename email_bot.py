import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'XXXXXXX@gmail.com'
email['subject'] = 'Hi i am just a robot created by xxxx'
email.set_content('Just testing things out')

with  smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('emailid@gmail.com', 'Your Password')
	smtp.send_message(email)
	print("All done!!!")