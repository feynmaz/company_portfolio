from django.db import models


class Company(models.Model):
    class Type(models.TextChoices):
        PRIVATE = 'частный',
        STATE = 'государственный'

    name = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Информация')
    assets = models.IntegerField(verbose_name='Активы (в млн. рублей)')
    type = models.CharField(max_length=20, choices=Type.choices, verbose_name='Тип')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
