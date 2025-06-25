from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),  # Home page of the CRUD app
    path('register/', views.register, name='register'),  # Register a new user
    path('login/', views.my_login, name='my-login'),  # Log in a user
    path('user-logout/', views.user_logout, name='user-logout'),  # Log out a user
    
    #CRUD operations for records
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('create-record/', views.create_record, name='create-record'),  # Create a new record
]