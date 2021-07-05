from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company


class UserProfile(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserCompanyRelationship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self) -> str:
        return str(self.company) + ' - ' + str(self.user)

    class Meta:
        verbose_name = 'Доступ'
        verbose_name_plural = 'Доступ'