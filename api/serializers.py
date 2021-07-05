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