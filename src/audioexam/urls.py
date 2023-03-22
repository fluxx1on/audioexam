from django.urls import include, path
from django.conf.urls.static import static

from config import settings
from . import views

urlpatterns = [
    path('', views.AudioList.as_view(), name='main'),
    path('create/', views.create_document, name='create_document'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)