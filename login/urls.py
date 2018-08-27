from django.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_form, name="login_form"),
    url(r'^login/$', views.login, name='login'),
]
