import os
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body):
    """
    Sends an email using SMTP credentials stored in GitHub Secrets.
    """

    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")

    if not smtp_email or not smtp_password:
        print("Missing SMTP credentials. Email not sent.")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_email
    msg["To"] = smtp_email  # sending to yourself

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(smtp_email, smtp_password)
            server.sendmail(smtp_email, [smtp_email], msg.as_string())

        print("Email sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")
