"""
Developer: Sam Skywalker
Purpose: Learning
Date: 12022.04.30:13:30

"""


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def simple_email():
    email = EmailMessage()
    email["from"] = "Your_Name"
    email["to"] = "example123@xyz.com"
    email['subject'] = "First Automated Email..."

    email.set_content("This is the first automated email ever created by myself ;)")

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('Your_Email', 'Your_Password')
        smtp.send_message(email)
        print('\n\t All Good, Email Sent :) \n')


# simple_email()


def second_email():
    email = EmailMessage()
    email['from'] = 'Your_Name'
    email['to'] = 'example123@xyz.com'
    email['subject'] = 'Second Automated Email...'

    # Content Specfic parameters
    email_content = Template(Path('content_one.html').read_text())
    email.set_content(email_content.substitute(name='Starboy', ai_system='Cortana AI'), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('Your_Email', 'Your_Password')
        smtp.send_message(email)
        print('\n\t Successful, Email Sent :) \n')


# second_email()

