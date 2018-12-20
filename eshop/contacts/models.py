from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s" % (self.state, self.address)
