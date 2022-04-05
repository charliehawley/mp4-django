from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


class Prompt(models.Model):
    # id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(null=False, blank=False)
    prompt = models.TextField(
        max_length=300, null=False, blank=False,
        unique=True, default="What's the crack?")
    slug = models.SlugField(max_length=200)

    def __int__(self):
        return self.date


# class User(models.Model):
#     name = models.CharField(max_length=30, null=False, blank=False)
#     password = models.CharField(max_length=30, null=False, blank=False)
#     top_subs = models.IntegerField(primary_key=False)
#     avatar = CloudinaryField('image', default='placeholder')

#     def __str__(self):
#         return str(self.name)


class Sub(models.Model):
    sub = models.TextField(max_length=150, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    prompt = models.ForeignKey(Prompt, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-upvotes']

    def __str__(self):
        return str(self.user)
