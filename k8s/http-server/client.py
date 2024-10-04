import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import time

# Настройки SMTP-сервера
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'hanasisgenya200710@gmail.com'
smtp_password = 'qlfi nnyx mmib rclg '

# Email получателя
recipient_email = 'hanasisgenya200710@gmail.com'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        text = msg.as_string()
        server.sendmail(smtp_user, recipient_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)

def check_server():
    try:
        response = requests.get('http://server:5000')
        if response.status_code == 200:
            return "Сервер запущен и работает."
        else:
            return f"Сервер вернул ошибку: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Не удалось подключиться к серверу: {e}"

while True:
    status = check_server()
    send_email("Отчет о состоянии сервера", status)
    time.sleep(3600)  # Отправлять отчет каждый час
