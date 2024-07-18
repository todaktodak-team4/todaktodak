from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.username