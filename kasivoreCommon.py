import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
import configfile


def sendmail(usubject, _msg, emaillist,_htmlBody =''):
    server = smtplib.SMTP_SSL(configfile.EMAIL_SERVER, configfile.EMAIL_PORT)

    # Next, log in to the server
    server.login(configfile.EMAIL_USER, configfile.EMAIL_PASS)

    # msg = MIMEText("""Hi, \n\n I think this will work. \n\n Regards""")
    msg = EmailMessage()    
    sender = configfile.EMAIL_USER
    recipients = emaillist.split(",")
    msg['Subject'] = usubject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg.set_content(_msg)

      
    _html = """\
       <!doctype html>

            <html lang="en">
            <head>
            <meta charset="utf-8">
            
            <style>
                .Header
                {
                    width: 100%;  
                    height: 100px;   
                    float: left;
                }
                .HeaderImage
                {
                    width: 100%; 
                    height: 100px;
                }
                .btnStyle
                {
                    background-color: #be222f; /* Green */
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    position: relative;
                    margin-left: 25%;
                    font-size: 16px;
                }
                @media screen and (max-width: 767px) {
                .HeaderImage
                {
                    height: 50px;
                }
                }
                
                
            </style>
            </head>

            <body>
            <div class="Header">
                <img src="https://kasivore.com/images/Backgroud/Headerbackgroud.jpg" class="HeaderImage">
            </div>
            <div class="maindiv">
                <div class="Content">
                
                <p>"""+_htmlBody + """
                

                </p>
                </div>
            </div>
            
                
            </div>
            </body>
            </html>
        """
    if _htmlBody !='':
        msg.add_alternative(_html, subtype= 'html')

    server.sendmail(sender, recipients, msg.as_string())
