from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="tracker_home"),
    path("games/new", views.create_game, name="create_game"),
    path("games/", views.list_games, name="list_games"),
    path("games/delete/<int:game_id>", views.delete_game, name="delete_game"),
]
