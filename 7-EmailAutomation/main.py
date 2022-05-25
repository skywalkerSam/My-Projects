"""
Developer: Sam Skywalker
Purpose: Email Automation
Date: 12022.05.25.13:38
"""

import pyfiglet
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def send_email():
    print(pyfiglet.figlet_format('Email  Sender', 'doom'))
    sender_name = input("\n Your Name: ")
    sender_email = input("\n Your Email Address: ")
    client_email = input("\n Client's Email Address: ")
    email_subject = input("\n Subject Of The Email: ")
    content_filename = input("\n Enter Content Filename: ")
    sender_email_key = input("\n Enter Your Security Key: ")

    email = EmailMessage()
    email['from'] = sender_name
    email['to'] = client_email
    email['subject'] = email_subject

    email_content = Template(Path(content_filename=='content_one.html').read_text())
    email.set_content(email_content.substitute(name='Starboy', ai_system='Cortana AI'), 'html')

    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_email_key)
        smtp.send_message(email)
        # print(f'Content Filename: {content_filename}')
        print('\n\t Successful, Email Sent :) \n')

    
    
try:
    if __name__ == "__main__":
        send_email()

except KeyboardInterrupt:
    print("\n\n\t Operation Cancelled By User :( \n")

except:
    print("\n\t Something went wrong! Please Try Again :( \n")
