from django.db import models
from product.models import Product, Category
import datetime
# from ckeditor_uploader.fields import RichTextUploadingField
# from phone_field import PhoneField
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=264)
    message = models.TextField()

    def __str__(self):
        return self.name + ", " + self.subject


class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=32)
    fullname = models.CharField(max_length=100, unique=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(
        max_length=500, unique=False, default='', blank=True)

    def __str__(self):
        return self.username
