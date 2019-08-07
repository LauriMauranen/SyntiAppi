from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
        path('', views.SyntiAppi, name='SyntiAppi'),
        path('<int:luku>/', views.SyntiAppi, name='SyntiAppi'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
