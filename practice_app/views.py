from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

from django.core.mail import send_mail

from django.http import HttpResponse


def home(request):
    return HttpResponse("hi baby")
https://github.com/NiteshSabbavarapu/practice_deployment.git