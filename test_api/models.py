from django.db import models
from pygments.lexers import get_all_lexers


# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]


class Deal(models.Model):
    customer = models.CharField(max_length=100, blank=True, default='')
    item = models.CharField(max_length=100, blank=True, default='')
    total = models.CharField(max_length=100, blank=True, default='')
    quantity = models.CharField(max_length=100, blank=True, default='')
    date = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['customer']
