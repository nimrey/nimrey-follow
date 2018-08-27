from django.contrib import admin
from django.urls import url, include

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', include('login.urls')),
]
