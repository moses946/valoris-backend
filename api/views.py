from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json
from . import models
import rest_framework.status

confirmation_template = "reply.txt"

@api_view(["POST"])
def contactForm(request):
    try:
        data = json.loads(request.body)
        print(f"data received {data}")
        first_name = data['firstName']
        last_name = data["lastName"]
        phone_number = data["phoneNumber"]
        email = data['email']
        message = data['projectDescription']
        company_name = data["companyName"]
        print("here")
        email_status = activateEmail("Message received", confirmation_template, email, first_name)
        if email_status==True:
            Lead = models.Lead.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, company = company_name, message=message)
            return Response({"message":"data received successfully"},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)





# function to confirmation mail 
def activateEmail(subject, template_path, to_email, name):
    print("inside email")
    mail_subject = subject
    
    message = render_to_string(template_path,{
        # 'user':user.username,
        'name': name
    })
    
    email = EmailMessage(mail_subject, message, to=[to_email])
   
    if email.send():
        print("email sent")
        return True
    else:
       print("email not sent")
       return False