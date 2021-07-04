from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from companies.models import Company


class CompaniesListView(ListView):
    model = Company
    template_name = 'companies/list.html'


class CompaniesDetailView(DetailView):
    model = Company
    template_name = 'companies/detail.html'
    fields = ['name', 'content', 'assets', 'type',]


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'companies/update_detail.html'
    fields = ['name', 'content', 'assets', 'type',]

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('companies:detail', kwargs={'pk': pk})



