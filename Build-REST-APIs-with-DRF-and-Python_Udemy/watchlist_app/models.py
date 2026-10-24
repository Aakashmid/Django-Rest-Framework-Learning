from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
