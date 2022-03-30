from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name,receiver):
    #creating message subject and sender
    subject = 'welcome to the moringa tribune newsletter'
    sender = 'john.waweru@student.moringaschool.com'

    #passing in hte context variables
    text_content = render_to_string('email/newsemail.txt', {"name":name})
    html_content = render_to_string('email/newsemail.html', {"name":name})

    msg = EmailMultiAlternatives(subject,text_content, sender,[receiver])

    msg.attach_alternative(html_content,'text/html')
    msg.send()