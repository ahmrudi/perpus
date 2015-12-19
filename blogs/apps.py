from django.apps import AppConfig
from django.conf.urls import url
from blogs import views

class BlogsConfig(AppConfig):
    name = 'blogs'


urlpatterns = [
    url(r'^$', views.home_page),
]