from django.urls import path
from .views import index_view, game_view, guessing_number_view

urlpatterns = [
    path('', index_view, name='index'),
    path('game/', game_view, name='game'),
    path('guessing/', guessing_number_view, name='guessing_number'),  
]


