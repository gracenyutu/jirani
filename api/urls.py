from django.urls import path
from . import views

urlpatterns = [
    path('prof/', views.getProfile, name='prof'),
    path('user/', views.getUser, name='user'),
    path('neighborhood/', views.getNeighborhood, name='neighborhood'),
    path('business/', views.getBusiness, name='business'),
    path('add/', views.addItem, name='add'),
]