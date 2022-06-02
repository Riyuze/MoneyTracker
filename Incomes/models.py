from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Income(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.TextField()
    source = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.source

    class Meta:
        ordering = ['-date']

class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

