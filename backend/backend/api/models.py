from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class SampleModel(models.Model):
    text = models.CharField(max_length = 180)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task