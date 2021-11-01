from django.urls import path
from .views import *

urlpatterns = [
    path('home/', show_smth, name='home'),
    path('player/<str:player_name>/', show_player),
    path('team/<str:team_name>/', show_team)
]

