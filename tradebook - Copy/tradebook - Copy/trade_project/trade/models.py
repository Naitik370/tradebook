from django.contrib.auth.models import User
from django.db import models
from datetime import date

class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Ticker = models.CharField(max_length=100)
    Quantity = models.FloatField(max_length=100)
    Entry = models.FloatField(max_length=100)
    Exit = models.FloatField(max_length=100)
    Date = models.DateField(default=date.today())
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)