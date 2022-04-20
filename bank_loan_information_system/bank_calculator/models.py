from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Months_To_Pay(models.Model):
    months = IntegerField(blank=True, null=True)

    def __str__(self):
        return self.months