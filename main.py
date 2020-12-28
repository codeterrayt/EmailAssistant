import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp.gmail.com" , 587)
server.starttls()


server_login_mail = "Your Email id "
server_login_password = "Your Password"

server.login(server_login_mail,server_login_password)


email = EmailMessage()

user_input_mail = input("Please Enter Email id ")
subject = input("Please Enter Your Subject")
message = input("Please Enter Message here")

email['From'] = server_login_mail
email['To'] = user_input_mail
email['Subject'] = subject
email.set_content(message)
server.send_message(email)

