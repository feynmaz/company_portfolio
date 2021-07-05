from django.db import models
from rest_framework.generics import ListAPIView, get_object_or_404, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination

from companies.models import Company
from .serializers import *


class CompanyListView(ListAPIView):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all().order_by('pk')
    pagination_class = PageNumberPagination


class CompanyDetailView(RetrieveUpdateAPIView):
    serializer_class = CompanyDetailSerializer
  
    def get_queryset(self):
        pk = self.kwargs['pk']
        company = Company.objects.filter(pk=pk)
        return company