import smtplib

user = input("Enter your gmail: ")
password = input("Enter your password: ")
target = input("Target mail: ")
msg = input("Message: ")

while True:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(user, target, msg)
    server.close()
    print('Successfully sent the mail!')