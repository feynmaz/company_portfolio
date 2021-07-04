from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

app_name = 'companies'

urlpatterns = [
    path(
        route='',
        view=CompaniesListView.as_view(),
        name='list',
    ),
    path(
        route='<int:pk>/',
        view=CompaniesDetailView.as_view(),
        name='detail'
    ),
    path(
        route='<int:pk>/update/',
        view=CompanyUpdateView.as_view(),
        name='update'
    )

]

urlpatterns += staticfiles_urlpatterns()