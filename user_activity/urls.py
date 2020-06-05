from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    url(r'get_json', views.UserActivity.as_view({'get': 'list'}), name='get_json'),
]