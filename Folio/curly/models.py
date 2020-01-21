from django.db import models

class Form(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.CharField(max_length=10)
    Phone = models.CharField(max_length=10)
    Message = models.CharField(max_length=30)

def __str__(self):
    return self.Name

