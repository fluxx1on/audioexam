import django.conf.urls.static
from django.urls import include, path

from config import settings
from . import views

urlpatterns = [
    path('', views.AudioList.as_view(), name='main'),
    path('create/', views.create_document, name='create_document'),
] + django.conf.urls.static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)