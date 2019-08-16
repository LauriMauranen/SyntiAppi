from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from synnit import views 


urlpatterns = [
    path('', views.Syntiappi.as_view()),
    path('kuvalla/', views.SyntiappiKuvalla.as_view(), name='syntiappi_kuvalla'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
