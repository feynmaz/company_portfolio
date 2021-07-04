from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company


class UserProfile(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserCompanyRelationship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'