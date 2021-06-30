from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^portfolio/', views.portfolio, name='portfolio'),
    re_path(r'^resume/', views.resume, name='menu_list'),
]