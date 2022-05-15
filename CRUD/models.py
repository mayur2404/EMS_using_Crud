from ctypes import addressof
import email
from unicodedata import name
from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    phone = models.IntegerField()


    def __str__(self):
        return self.name
    