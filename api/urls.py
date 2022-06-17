from django.urls import path
from . import views

urlpatterns = [
    path('prof/', views.getProfile, name='prof'),
    path('user/', views.getUser, name='user'),
]