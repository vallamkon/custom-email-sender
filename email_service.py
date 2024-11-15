import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import random

class EmailService:
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'  # Change based on your ESP
        self.smtp_port = 587
        self.email_account = 'your-email@gmail.com'
        self.email_password = 'your-email-password'

    def send_emails(self, data):
        sent_count = 0
        for row in data:
            # Generate the email body using row data and prompt
            subject = row['Company Name'] + " - " + row['Product']
            body = f"Hello {row['Company Name']}, we offer {row['Product']}."
            self._send_email(row['Email'], subject, body)
            sent_count += 1
            time.sleep(random.uniform(1, 3))  # Throttling
        return {"sent": sent_count}

    def _send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email_account
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email_account, self.email_password)
            server.sendmail(self.email_account, to_email, msg.as_string())
