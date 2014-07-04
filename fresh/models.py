from django.db import models

# Create your models here.


class Fresh(models.Model):
    title = models.CharField(max_length=50, help_text='fresh title')
