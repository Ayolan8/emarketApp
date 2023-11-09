from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="item_image")
    is_sold = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.title