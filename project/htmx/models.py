import math
from django.db import models
import random

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)