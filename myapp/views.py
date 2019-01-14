from django.http import HttpResponse
from django.shortcuts import render
from cproject.tasks import create_random_user_accounts
# Create your views here.

def createusers(request):
    a = create_random_user_accounts.delay(2)
    print(type(a))
    return HttpResponse("Creating")