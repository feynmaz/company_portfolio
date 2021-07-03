from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company


class Role(models.Model):
    class RoleName(models.TextChoices):
        ADMIN = 'admin',
        USER = 'user'

    name = models.CharField(max_length=10, choices=RoleName.choices)


class UserProfile(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserCompanyRelationship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default='user')