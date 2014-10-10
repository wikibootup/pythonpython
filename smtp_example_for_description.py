#!/usr/bin/env python
import smtplib
import os 

sender = "sender@gmail.com"
sender_pwd = os.environ['SENDER_PASSWORD']
receiver = "receiver@gmail.com"
smtpObj = smtplib.SMTP("smtp.gmail.com",587)

subject_name = "From my test"
contents = "Hi"

smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender, sender_pwd)

msg = 'Subject: %s\n\n%s' % (subject_name, contents)

try:
    smtpObj.sendmail(sender, receiver, msg)
except smtplib.SMTPException:
    print "SMTP AUTHENTICATION failed"
else:
    print 'done!'

smtpObj.close()

