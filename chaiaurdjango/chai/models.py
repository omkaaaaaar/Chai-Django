from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai')
    date_added = models,models.DateTimeField(default=timezone.now)
    