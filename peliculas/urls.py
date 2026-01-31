from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('anterior/<int:page>', views.anterior, name='anterior'), 
    path('siguiente/<int:page>', views.siguiente, name='siguiente'),
] 