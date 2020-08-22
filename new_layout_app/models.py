from django.db import models

# Create your models here.
class destination(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField(default='')
    offer = models.BooleanField(default=False)