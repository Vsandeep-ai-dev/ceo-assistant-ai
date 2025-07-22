import os
import base64
import openai
import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# ----------------------
# AUTHENTICATE GMAIL
# ----------------------
def authenticate_gmail():
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/gmail.modify"])
    service = build("gmail", "v1", credentials=creds)
    return service

# ----------------------
# FETCH EMAILS
# ----------------------
def get_recent_emails(service, max_results=5):
    results = service.users().messages().list(userId="me", maxResults=max_results).execute()
    messages = results.get("messages", [])
    email_texts = []

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        snippet = msg_data.get("snippet", "")
        email_texts.append(snippet)

    return email_texts

# ----------------------
# GENERATE SMART REPLY
# ----------------------
def generate_email_reply(email_text, tone="professional"):
    prompt = f"""
You are an executive assistant. Read the following email and reply in a {tone} tone.

Email:
\"\"\"{email_text}\"\"\"

Reply:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful email-writing assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()

# ----------------------
# SEND EMAIL
# ----------------------
def send_email(service, to_email, subject, body):
    message = MIMEMultipart()
    message["to"] = to_email
    message["subject"] = subject

    message.attach(MIMEText(body, "plain"))

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message_body = {"raw": raw}

    sent = service.users().messages().send(userId="me", body=message_body).execute()
    return sent

