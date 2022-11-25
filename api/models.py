from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Book(models.Model):
    ISBN = models.CharField('ISBN',max_length=255)
    title = models.CharField('Title',max_length=255)
    author = models.CharField('Author',max_length=255)
    published = models.IntegerField(
        'Published Year',
        validators=[
            MinValueValidator(1500),
            MaxValueValidator(datetime.date.today().year),
        ],
        help_text="YYYY",
    )
    publisher = models.CharField('Publisher',max_length=255)
    price = models.IntegerField('Price')
    available = models.IntegerField('No of Books Available')
    
