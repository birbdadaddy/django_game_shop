from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game1/', views.game1, name='game1'),
    path('game2/', views.game2, name='game2'),
    path('add_points/', views.add_points, name='add_points'),
    path('shop/', views.shop, name='shop'),
]