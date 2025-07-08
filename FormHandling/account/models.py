from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    email = models.EmailField(max_length=120, unique=True, blank=False, null=False)
    username = models.CharField(max_length=120, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)    
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'accounts_customuser'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        constraints = [
            models.UniqueConstraint(fields=['username', 'email'], name='unique_username_email'),
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_first_and_last_name')
        ]