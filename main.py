import ssl
from smtplib import SMTP
from email.message import EmailMessage
from getpass import getpass

fromaddr = input("sender's adress: ")
toaddrs = input("receiver's adress: ")
msg = EmailMessage()
msg['From'] = fromaddr
msg['To'] = toaddrs
msg['Subject'] = "Sent via Python smtplib"
msg.set_content("Siema Krzychu")
password = getpass(prompt="type password: ")

try:
    context = ssl.create_default_context()
    with SMTP("smtp.mail.me.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        smtp.login(fromaddr,password)
        smtp.sendmail(fromaddr,toaddrs,msg.as_string())
except Exception as e:
    print(e)
