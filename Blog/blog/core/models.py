from django.db import models
from uuid import uuid4
from accounts.models import CustomUser


def upload_to(instance, filename):
    base, ext = filename.split('.')
    return f'files/{instance.user.username}/{base}.{ext}'


class Post(models.Model):
    
    uuid    = models.UUIDField(unique=True, default=uuid4)
    title   = models.CharField(unique=True, max_length=180)
    content = models.TextField()
    banner  = models.ImageField(upload_to=upload_to) 
    author  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @property
    def rating(self):
        return self.review_set.aggregate(models.Avg('stars'))['stars__avg'] or 0


STAR_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]


class Review(models.Model):
    
    author  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    stars   = models.IntegerField(choices=STAR_CHOICES, default=3)

