# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('coin-flip/', views.coin_flip, name='coin_flip'),
    path('dice-roll/', views.dice_roll, name='dice_roll'),
    path('random-number/', views.random_number, name='random_number'),
]
