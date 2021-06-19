#references
#https://www.code-learner.com/python-send-html-image-and-attachment-email-example/
#https://www.codegrepper.com/code-examples/python/how+to+send+images+to+gmail+or+phone+through+python+program

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_warning():
    mail_content = '''Hello, someone might have 
    entered your house please check
    '''
    #The mail addresses and password
    sender_address = 'robomansaha@gmail.com'
    sender_pass = 'xx' #password here
    receiver_address = 'homagnisaha@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Someone has entered #2307 - see picture attached.'
    # attache a MIMEText object to save email content
    msg = message
    msg_content = MIMEText('send with attachment...', 'plain', 'utf-8')
    msg.attach(msg_content)
    # to add an attachment is just add a MIMEBase object to read a picture locally.
    with open('person.png', 'rb') as f:
        # set attachment mime and file name, the image type is png
        mime = MIMEBase('person', 'png', filename='person.png')
        # add required header data:
        mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
        mime.add_header('X-Attachment-Id', '0')
        mime.add_header('Content-ID', '<0>')
        # read attachment file content into the MIMEBase object
        mime.set_payload(f.read())
        # encode with base64
        encoders.encode_base64(mime)
        # add MIMEBase object to MIMEMultipart object
        msg.attach(mime)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #enable security
    #server.set_debuglevel(1)
    server.login(sender_address, sender_pass)
    server.sendmail(sender_address, [receiver_address], msg.as_string())
    server.quit()
    print('Mail Sent')
