from django.db import models
from django.db.models import Model


# Create your models here.

class CsvModel(Model):
    csv_fields = models.FileField()
