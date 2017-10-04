import smtplib

def sendEmail(addressFrom, addressTo, msg):
    server = smtplib.SMTP('localhost.com')
    server.set_debuglevel(1)
    server.sendmail(addressFrom, addressTo, msg)
    server.quit()


msg = "This is the content of the email"
addressFrom = "ben629dx@gmail.com"
addressTo = "ben659dx@gmail.com"

sendEmail(addressFrom, addressTo, msg)