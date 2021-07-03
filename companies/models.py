from django.db import models


class Company(models.Model):
    class Type(models.TextChoices):
        PRIVATE = 'частный',
        STATE = 'государственный'

    name = models.CharField(max_length=200)
    content = models.TextField()
    assets = models.IntegerField()
    type = models.CharField(max_length=20, choices=Type.choices)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
