from django.db import models

# Create your models here.
class Lembrete(models.Model):
    lembrete = models.CharField(max_length=150)