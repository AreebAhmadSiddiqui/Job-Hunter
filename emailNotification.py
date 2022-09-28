import smtplib  
from email.message import EmailMessage  
import os

def email_alert(subject,body,to,time):

    user=os.environ.get('dev-user-email')
    password=os.environ.get('dev-pass')
    
    
    msg=EmailMessage()
    
    msg['Subject']=subject
    msg['To']=to 
    msg['From']=user
    msg.set_content(body)

    with open(f'Job-Data({time}).csv','rb') as f:
        file_data=f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()