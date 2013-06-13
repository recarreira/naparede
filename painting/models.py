from django.db import models

# Create your models here.

class Painting(models.Model):
    title           = models.CharField('Title', max_length=200, null=False)
    description     = models.TextField('Description', null=False)