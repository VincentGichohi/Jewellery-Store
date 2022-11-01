from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name='Nearest Location')
    city = models.CharField(max_length=150, verbose_name='State')
    
    def __str__(self) -> str:
        return self.locality
    