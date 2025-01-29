from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="tracker_home"),
    path("create/game", views.create_game, name="create_game"),
]
