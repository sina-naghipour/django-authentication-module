from django.db import models
from account.models import CustomUser
from django.utils.text import slugify
from django.db.models.constraints import UniqueConstraint



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='slug', unique=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


def upload_path(instance, filename):

    return f'files/user_{instance.author.id}/{filename}'


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLSIHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'
        

    title = models.CharField(max_length=130)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=14, choices=StatusChoices.choices, default=StatusChoices.PUBLSIHED)
    image = models.ImageField(verbose_name='post_image', upload_to=upload_path)
    tags = models.ManyToManyField(Category, related_name='posts')
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
        constraints = [
            UniqueConstraint(fields=['title'], name='unique_title'),
        ]