# OTP to mail

import smtplib
import random

sender = "sahilpawar7719881716@gmail.com"
password = "vzkq xigo ujug csxl"
receiver = "mercy30032003@gmail.com"
body = "Your OTP is " + str(random.randint(100000, 999999)) + ". Valid for next 15 minutes."

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender, password)

server.sendmail(sender, receiver, body)

print("Mail sent")