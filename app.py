from flask import Flask, request, jsonify
from email_service import EmailService
from utils import load_data_from_csv, schedule_email, send_email

app = Flask(__name__)

@app.route('/connect', methods=['POST'])
def connect_email():
    # Logic for email account connection (OAuth, SMTP)
    pass

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.json
    # Use EmailService to send email
    email_service = EmailService()
    result = email_service.send_emails(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
