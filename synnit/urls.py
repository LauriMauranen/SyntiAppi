from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from synnit import views 


urlpatterns = [
    path('', views.Syntiappi.as_view()),
    path('taulukko/', views.lataa_csv)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
