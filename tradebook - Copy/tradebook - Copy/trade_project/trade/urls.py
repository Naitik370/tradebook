from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('list/', views.trade_list, name='trade_list'),
    path('add/', views.add_trade, name='add_trade'),
]