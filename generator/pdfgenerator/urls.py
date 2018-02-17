from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.generate, name='generate'),
    url(r'^$', views.download_file, name='download_file'),
    url(r'^$', views.list, name='list'),

]