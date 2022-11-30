from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('about/', views.about),
    path('history/', views.history),
    path('contact/', views.contact),
]
