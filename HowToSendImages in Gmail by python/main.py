import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

from_address="Sender _username"
password="Your email password"
to_address="reciever password"


#### Writing content of the mail
msg = MIMEMultipart()    
msg['From'] = from_address
msg['To'] = to_address 
msg['Subject'] = "3rd Tutorial on mailing System"
body = "Sending one or more images"
msg.attach(MIMEText(body, 'plain')) 

# for attaching the images

filename=["applicant-tracking-system-138k.png","dog1.jpeg","dog2.jpg"]
for i in filename:
    reading=open(i,"rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((reading).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment",filename=i)
    msg.attach(p)

## Starting the main work
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.ehlo()
s.starttls() 
 
s.login(from_address, password) 
   
text = msg.as_string() 

s.sendmail(from_address, to_address, text) 

s.quit() 
