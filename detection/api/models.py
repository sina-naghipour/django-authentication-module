from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime
import os
from django.core.validators import FileExtensionValidator

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user



class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_name'),
        ]




def upload_to(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'files/{instance.owner.username}/{datetime.now().strftime('%Y-%m')}/{base_filename}.{file_extension}'


class Image(models.Model):
    file = models.FileField(upload_to=upload_to, validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'webp'],
            message='Unsupported file extension. Allowed: jpg, jpeg, png, gif, webp'
        )
    ],
    help_text='Allowed formats: JPG, JPEG, PNG, GIF, WEBP (Max 10MB)')
    
    owner = models.ForeignKey(CustomUser, models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'