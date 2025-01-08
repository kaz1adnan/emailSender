import smtplib
import ssl
from email.message import EmailMessage

subject = "Automated Python Email"
body = "This is a test email from Python"
senderEmail = "xyz@gmail.com"
receiverEmail = "xyz@gmail.com"
password = input("Enter your password: ")

message = EmailMessage()
message["From"] = senderEmail
message["To"] = receiverEmail
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Mail is being delivered...")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(senderEmail, password)
    server.sendmail(senderEmail, receiverEmail, message.as_string())

print("Successfully sent!")

#Code no more works after February 2025 due to Google Security Updates