import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time

# Email you want to send the update from (only works with gmail)
fromEmail = 'smartcctvp@gmail.com'
# An app password here to avoid storing password in plain text
fromEmailPassword = 'xhncobtyuigkckcy'

# Email you want to send the update to
toEmail = 'cleven.theorizchy@gmail.com'

def sendEmail(image):
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = '[SMART CCTV] Security Alert!'
	msgRoot['From'] = fromEmail
	msgRoot['To'] = toEmail
	msgRoot.preamble = 'Unknown person detected in your premises'

    # Create the email body text with the time in bold
	current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	body_text = f"Smart security cam found an unknown person within your premises at <b>{current_time}</b>"
	msgText = MIMEText(body_text, 'html')
	msgRoot.attach(msgText)

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('<img src="cid:image1">', 'html')
	msgAlternative.attach(msgText)

	msgImage = MIMEImage(image)
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
	smtp.quit()