from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField()
    video = models.FileField()
    delivered = models.BooleanField(default=False)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='seller')
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True,
                              blank=True, related_name='buyer')
    session_id = models.CharField(max_length=32, blank=True, null=True)