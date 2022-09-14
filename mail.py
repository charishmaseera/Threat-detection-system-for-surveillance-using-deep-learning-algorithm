
# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
import time
  
# creates SMTP session
def mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
    s.starttls()
  
# Authentication
    s.login("18jg1a0420.charishma@gvpcew.ac.in", "Cherry@2001")
  
# message to be sent
    message = message
  
# sending the mail
    s.sendmail("18jg1a0420.charishma@gvpcew.ac.in", "charishma.seera4@gmail.com", message)
  
# terminating the session
    s.quit()

