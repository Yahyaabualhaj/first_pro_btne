from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    return send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)