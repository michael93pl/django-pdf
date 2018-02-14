from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.get_name, name='get_name'),
    #url(r'^$', views.download_file, name='download_file')

]