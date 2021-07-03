from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import LoginUserView, RegisterUserView

app_name = 'users'

urlpatterns = [
    path(
        route='login/',
        view=LoginUserView.as_view(),
        name='login',
    ),
    path(
        route='register/',
        view=RegisterUserView.as_view(),
        name='register',
    ),
    path('', include('django.contrib.auth.urls')),
    # 'logout/' [name='logout']

]

urlpatterns += staticfiles_urlpatterns()