from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('upload/', views.upload, name='upload'),
    path('search/', views.search, name='search'),
    path('newhood/', views.newhood, name='new-hood'),
    path('joinhood/<id>', views.joinahood, name='join-hood'),
    path('leavehood/<id>', views.leaveahood, name='leave-hood'),
    path('hoods/', views.hoods, name='jirani'),
]
