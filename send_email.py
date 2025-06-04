import smtplib, ssl
import os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    user = os.getenv("EMAIL")

    password = os.getenv("python_passw_google")

    receiver = os.getenv("EMAIL")
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)

