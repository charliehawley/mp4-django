from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    date = models.DateField(auto_now=True)
    prompt = models.TextField(max_length=300,
                              null=False, blank=False,
                              unique=True, default="What's the crack?")
    slug = models.SlugField(max_length=200, unique=True)
    subs_list = models.ManyToManyField(
        User, related_name='prompt_sub', blank=True)

    def __int__(self):
        return self.date


class Sub(models.Model):
    sub = models.TextField(max_length=150, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(User, related_name='sub_upvote',
                                     blank=True)
    prompt = models.ForeignKey(Prompt, default=None, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.user)

    def number_of_upvotes(self):
        return self.upvotes.count()
