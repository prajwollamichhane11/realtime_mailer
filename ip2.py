import smtplib
import time
import subprocess as sp

def get_ip():
    return sp.getoutput('dig +short myip.opendns.com @resolver1.opendns.com').split()[0]

new_ip = get_ip()
print(new_ip)


def email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your email", "email password")
    
    msg = new_ip
    server.sendmail("sender", "receiver", msg)
    server.quit()

email()    

current_ip = new_ip
    
while True:
    
    if (current_ip == get_ip()):
        time.sleep(60)
        
    else:
        email()


    
