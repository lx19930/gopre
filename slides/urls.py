from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_slide, name='upload_slide'),
    path('', views.slide_list, name='slide_list'),
]
