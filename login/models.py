from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return 'Username: ' + self.username + ' | Password: ' + self.password
