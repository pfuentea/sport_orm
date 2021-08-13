from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	baseball_liga=League.objects.filter(sport='Baseball').all()
	ligas_femeninas=League.objects.filter(name__contains='Women').all()
	ligas_hockey=League.objects.filter(sport__contains='hockey').all()
	ligas_no_futbol=League.objects.exclude(sport='Football').all()
	ligas_conferencia=League.objects.filter(name__contains='conference').all()
	ligas_atlantica=League.objects.filter(name__contains='atlantic').all()
	ligas_dallas=[liga for liga in  League.objects.all() if liga in Team.objects.all().filter(location='Dallas')]

	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_liga":baseball_liga,
		"ligas_femeninas":ligas_femeninas,
		"ligas_hockey":ligas_hockey,
		"ligas_no_futbol":ligas_no_futbol,
		"ligas_conferencia":ligas_conferencia,
		"ligas_atlantica":ligas_atlantica,
		"ligas_dallas":ligas_dallas
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")