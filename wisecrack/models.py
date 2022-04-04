from django.db import models


class Crack(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    text = models.TextField(max_length=150, null=False, blank=False)

    def __int__(self):
        return self.date


class User(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    top_subs = models.IntegerField(primary_key=False)
