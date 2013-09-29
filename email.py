import smtplib
from email.mime.text import MIMEText

"""This function is used to send an email through
the local smtp server. All parameters can be filled
using plain text.
e.g. sender = "me@example.com"
receiver = "you@example.com"
subject = "example email message"
text = "this is an example"
"""

def sendEmail(sender, receiver, subject, text)
	
	msg = MIMText(text)
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = receiver
	
	s = smtplib.SMTP('localhost')
	s.sendmail(sender, [receiver], msg.as_string())
	s.quit
	

# http://docs.python.org/2/library/email-examples.html
