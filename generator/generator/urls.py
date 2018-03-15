from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from pdfgenerator import views
from pdfgenerator.views import Index, Generate, List
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^generate/', Generate.as_view(), name='generate'),
    url(r'^list/', List.as_view(), name='list'),
    url(r'^download/(?P<file_name>.+)$', views.download_file, name='download_file')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

