
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS

    path('', include('companies.urls')),
    path('users/', include('users.urls')),

    path('api/v1/', include('api.urls')),

    
]