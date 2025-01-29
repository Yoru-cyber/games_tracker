from django.http import HttpResponse
from django.shortcuts import redirect, render

from games_tracker_app.forms import GameForm


# Create your views here.
def home(request):
    return render(request, "index.html")


def create_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker_home")  # Redirect to a list view or another page
    else:
        form = GameForm()
    return render(request, "create_game.html", {"form": form})
