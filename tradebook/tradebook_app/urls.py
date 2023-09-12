from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('',views.home, name='home')
    # Add more URL patterns for your app as needed.
]
