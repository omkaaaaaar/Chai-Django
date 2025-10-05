from django.db import models
from django.utils import timezone

# Create your models here.
CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER '),
    ('KI', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),  
]


class ChaiVariety(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)

def __str__(self):           #ISSSUE OVERR HHEEERRRREEEEEE !!!!!!!!!
    return self.name         #ISSSUE OVERR HHEEERRRREEEEEE !!!!!!!!! ep 5, models django aur chai, time - 25min