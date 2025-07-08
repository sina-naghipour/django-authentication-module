from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    
    email = models.EmailField(max_length=120, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active']

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        db_table = 'accounts_customuser'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='full_name')
        ]

        ordering = ['-date_joined']
        
        
