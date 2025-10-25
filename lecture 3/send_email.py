import smtplib
from email.mime.text import MIMEText

email_address = "boris.r.boyanski.2024@elsys-bg.org"
email_password = ""  
to_email = "ddimitrov@elsys-bg.org"  

body = f"Хей!\n\nИмаме нещо ново, което прави нещата по-лесни и по-бързи.\nНяма сложности, няма излишни обяснения — просто работи.\n\nАко ти звучи добре, пиши.\n\nПоздрав,\nБорис Боянски"
message = MIMEText(body)
message["From"] = email_address
message["To"] = to_email
message["Subject"] = "Python Email"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(email_address, email_password)
    server.send_message(message)

print("✅ Email sent successfully.")
