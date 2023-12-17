import smtplib
import getpass

smtp = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp.ehlo())

print(smtp.starttls())

email = getpass.getpass('Email: ')
password = getpass.getpass("Password: ")

print(smtp.login(email, password))

from_address = email
to_address = getpass.getpass("To emails: ")
final_message = "Subject: Python Message\nThe first message sent from python. Congratulations!"

print(smtp.sendmail(from_address, to_address, final_message))
