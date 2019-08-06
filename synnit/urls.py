from django.urls import path

from . import views

urlpatterns = [
        path('', views.SyntiAppi, name='SyntiAppi'),
]
