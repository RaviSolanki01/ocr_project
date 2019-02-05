from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name = 'ImageToText-home'),
    path('image/', views.image , name = 'ImageToText-home'),
]