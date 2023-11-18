from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    message = models.TextField(max_length=255)
    