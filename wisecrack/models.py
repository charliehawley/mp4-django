from django.db import models

# Create your models here.
class Crack(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    crack = models.CharField(max_length=150, null=False, blank=False)