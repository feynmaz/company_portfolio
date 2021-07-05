from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from companies.models import Company


class CompanyListView(ListView):
    model = Company
    paginate_by = 5
    template_name = 'companies/list.html'


class CompanyBase:
    model = Company
    fields = ['name', 'content', 'assets', 'type',]


class CompanyDetailView(CompanyBase, DetailView):
    template_name = 'companies/detail.html'
    

class CompanyUpdateView(CompanyBase, UpdateView):
    template_name = 'companies/update_detail.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('companies:detail', kwargs={'pk': pk})



