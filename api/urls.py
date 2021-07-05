from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import CompanyDetailView, CompanyListView

app_name = 'api'

urlpatterns = [

    path(
        route='companies/',
        view=CompanyListView.as_view(),
        name='list',
    ),
    path(
        route='companies/<int:pk>/',
        view=CompanyDetailView.as_view(),
        name='detail',
    ),

]

urlpatterns += staticfiles_urlpatterns()