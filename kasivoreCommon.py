import smtplib
from email.mime.text import MIMEText
import configfile


def sendmail(usubject, msg, emaillist):
    server = smtplib.SMTP(configfile.EMAIL_SERVER, configfile.EMAIL_PORT)

    # Next, log in to the server
    server.login(configfile.EMAIL_USER, configfile.EMAIL_PASS)

    # msg = MIMEText("""Hi, \n\n I think this will work. \n\n Regards""")
    msg = MIMEText(msg)
    sender = configfile.EMAIL_USER
    recipients = emaillist.split(",")
    msg['Subject'] = usubject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    server.sendmail(sender, recipients, msg.as_string())
