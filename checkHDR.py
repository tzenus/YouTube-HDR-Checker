import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def check_available_formats(url):
    command = ["youtube-dl", "-F", url]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error has occurred: {e.stderr}"

def send_email(smtp_server, smtp_port, smtp_username, smtp_password, to_email, subject, body, video_url):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    body_with_url = f"{body}\n\nURL: {video_url}"
    msg.attach(MIMEText(body_with_url, 'plain'))

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())
        server.quit()
        print("The email was sent successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        return False

# Your SMTP data (replace with yours)
smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username = "your_email@gmail.com"
smtp_password = "your_password"
to_email = "email_recipient@gmail.com"

# Video URL to check HDR
url_to_check = "https://youtu.be/S6sGYAd2jLA"

# Check period in seconds
check_interval_seconds = 3600

while True:
    result = check_available_formats(url_to_check)

    if "HDR" in result:
        subject = "HDR detected in video!"
        body = "HDR is available in video. Check it out for yourself!"
        if send_email(smtp_server, smtp_port, smtp_username, smtp_password, to_email, subject, body, url_to_check):
            break  # Break the loop if the email is sent successfully

    print(result)
    time.sleep(check_interval_seconds)
