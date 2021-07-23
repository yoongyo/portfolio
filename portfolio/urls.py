from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.portfolio, name='portfolio'),
    re_path('ably', views.ably_portfolio, name='portfolio_ably')
    # re_path(r'^$', views.resume, name='resume'),
]