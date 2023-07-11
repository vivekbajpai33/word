from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
    # phone_number = models.CharField(max_length=20,unique=True)
    # email_user = models.CharField(max_length=100,null=True)
    # username = None

    # USERNAME_FIELDS = 'phone_number'
    # REQUIRED_FIELDS = ''

class user(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=70)
    dp = models.FileField(upload_to="name/")

 


# Create your models here.
