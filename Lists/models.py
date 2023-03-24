from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)


    def __str__(self):
        return self.name


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    body = models.CharField('New Item',max_length=50)

    def __str__(self):
        return self.body[0:50]