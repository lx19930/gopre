
# Create your models here.
from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='slides/')

    def __str__(self):
        return self.title