from django.db import models
from uuid import uuid4


    

class Product(models.Model):
    
    uuid        = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name        = models.CharField(max_length=180, unique=True)
    description = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    owner       = models.CharField(max_length=150)
    quantity    = models.PositiveIntegerField()
    
    @property
    def in_stock(self):
        return self.quantity > 0
    
    @property
    def reviews(self):
        return self.review_set.all()
    
    @property
    def rating(self):
        return self.review_set.aggregate(models.Avg('stars'))['stars__avg'] or 0



    
class Review(models.Model):
    
    user_name = models.CharField(max_length=180, unique=True)
    stars     = models.IntegerField(choices=[(int(i), str(i)) for i in range(1,6)])
    timestamp = models.DateTimeField(auto_now_add=True)
    content   = models.TextField()
    product   = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ['-timestamp']


