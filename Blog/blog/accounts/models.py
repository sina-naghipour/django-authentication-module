from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    email      = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    timestamp  = models.DateTimeField(auto_now_add=True)
    is_staff   = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_name')
        ]