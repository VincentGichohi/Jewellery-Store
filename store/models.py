from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name='Nearest Location')
    city = models.CharField(max_length=150, verbose_name='State')
    
    def __str__(self) -> str:
        return self.locality
    
    
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Category Title')
    slug = models.SlugField(max_length=50, verbose_name='Category Slug')
    description = models.TextField(blank=True, verbose_name='Category Description')
    category_image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Category Image")
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering= ('-created_at', )
        
    def __str__(self) -> str:
        return self.title
    
    