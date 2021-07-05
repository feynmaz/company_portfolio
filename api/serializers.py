from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from companies.models import Company


class CompanyListSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('pk', 'name')
         

class CompanyDetailSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('pk', 'name', 'content', 'assets', 'type', )