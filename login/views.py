from django.shortcuts import render
from django.http import HttpResponse

from .models import Account


def login_form(request):
    return render(request, 'login/login_form.html')


def login(request):
    get = request.POST.get
    account = Account.objects.create(
        username=get('username'),
        password=get('password')
    )
    return render(request, 'login/home.html')
