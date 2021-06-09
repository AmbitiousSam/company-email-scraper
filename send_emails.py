# -*- coding: utf-8 -*-

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

fromEmail - "18r01a05e2@cmritonline.ac.in"
# email - "passing emails from csv"
subject - "Free Merch or Coupons"
message - '''Hi,

My name is Siva Kumar

I just wanted to say that I’m a huge fan of your company. I love your product and services.

As someone who’s been a loyal customer for years, I just wanted to say you’re doing great work!

I was also wondering if you have any samples or coupons or any free merch you could send my way – I’d love to try more of your products and would appreciate anything you could send me.

Below is my address:

DN-41, Devi Nagar, Neredmet, RK. Puram, Secunderabad, Hyderabad, Teleangana, India - 500056

Thank you so much and have a great day!

'''


def send_email(fromEmail, email, subject, message):
    message = Mail(
        from_email=fromEmail,
        to_emails=email,
        subject=subject,
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get(YOUR_SENDGRID_API_KEY))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


with open('emails.csv', 'r') as emails:
    count = 1
    for email in emails:
        print(str(count) + ': ', email)
        send_email('your-email', email, 'your-subject-line', 'your-message')
        count = count + 1
