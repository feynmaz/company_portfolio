from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView


from companies.models import Company


class CompaniesListView(ListView):
    model = Company
    template_name = 'companies/list.html'


class CompaniesDetailView(DetailView):
    model = Company
    template_name = 'companies/detail.html'

