import smtplib
import config
#sender_email = "qmazhar@gmail.com"
#rec_email = "azharqurashi77@gmail.com"
#password = input(str("enter the password : "))
#message = "Hey email send from python"

#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login(sender_email,password)
#print ("Login Success")
#server.sendmail(sender_email,rec_email,message)
#print ("email has been sent ti ", rec_email)

def send_email(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.PASSWORD,message)
        server.quit()
    except:
        print("sent email")
subject = "Test Subject"
msg = "Hello there "
send_email(subject,msg)




