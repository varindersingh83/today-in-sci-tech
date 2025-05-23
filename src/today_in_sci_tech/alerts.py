"""
Module for sending alerts and notifications.
"""

import os
import re
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_sms_alert(subject: str, body: str) -> None:
    """
    Send an SMS alert using email-to-SMS gateway.
    
    Args:
        subject: Alert subject
        body: Alert message body
    """
    sender = os.getenv("ALERT_EMAIL")
    password = os.getenv("ALERT_EMAIL_PASS")
    receiver = os.getenv("ALERT_SMS_GATEWAY")

    # Remove emojis and limit length
    clean_body = re.sub(r'[^\x00-\x7F]+', '', subject + " - " + body)
    clean_body = clean_body[:160]

    msg = MIMEText(clean_body)
    msg["Subject"] = subject[:30]
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("✅ SMS alert sent")
    except Exception as e:
        print("❌ Failed to send SMS alert:", str(e)) 