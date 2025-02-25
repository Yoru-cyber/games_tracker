from django.http import HttpResponse, request
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count, Q
from games_tracker_app.forms import GameForm
from games_tracker_app.models import Game


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


def list_games(request):
    games = Game.objects.order_by("id").all()  # Fetch all items
    paginator = Paginator(games, 10)  # Show 10 items per page
    page_number = request.GET.get("page")  # Get the current page number from the URL
    page_obj = paginator.get_page(
        page_number
    )  # Get the Page object for the current page
    return render(request, "list_games.html", {"page_obj": page_obj})


def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect("list_games")


def update_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        form = GameForm(request.POST, None, instance=game)
        if form.is_valid():
            form.save()
            return redirect("list_games")
    else:
        form = GameForm(instance=game)
        return render(request, "update_game.html", {"form": form})


def stats(request):
    results = (
        Game.objects
        .aggregate(
            playing=Count("id", filter=Q(status="PLAYING")),
            plan_to_play=Count("id",filter=Q(status="PLANTOPLAY")),
            finished=Count("id",filter=Q(status="FINISHED")),
        )
    )
    data = {"total": results.get("playing")+results.get("plan_to_play")+results.get("finished"), "playing": results.get("playing"), "plan_to_play": results.get("plan_to_play"), "finished": results.get("finished")}
    return render(request, "stats.html", {"data": data})
