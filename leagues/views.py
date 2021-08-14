from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from . import team_maker

def index(request):
	baseball_liga=League.objects.filter(sport='Baseball').all()
	ligas_femeninas=League.objects.filter(name__contains='Women').all()
	ligas_hockey=League.objects.filter(sport__contains='hockey').all()
	ligas_no_futbol=League.objects.exclude(sport='Football').all()
	ligas_conferencia=League.objects.filter(name__contains='conference').all()
	ligas_atlantica=League.objects.filter(name__contains='atlantic').all()
	ligas_dallas=League.objects.filter(teams__location='Dallas')
	teams_raptors=Team.objects.filter(team_name__contains='raptor').all()
	teams_city=Team.objects.filter(location__contains='city').all()
	teams_t=Team.objects.filter(location__startswith='t').all()
	#10
	teams_order_location=Team.objects.all().order_by('location')
	teams_order_team_inv=Team.objects.all().order_by('-team_name')
	jugadores_cooper=Player.objects.filter(last_name__contains='Cooper').all()
	jugadores_joshua=Player.objects.filter(first_name__contains='Joshua').all()
	jugadores_cooper_joshua=[pl for pl in Player.objects.filter(last_name__contains='Cooper').all() if pl not in jugadores_joshua]
	jugadores_alex_wyatt=Player.objects.filter(Q(first_name__contains='Wyatt')|Q(first_name__contains='Alexander')).all()

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
		"ligas_dallas":ligas_dallas,
		"teams_raptors":teams_raptors,
		"teams_city":teams_city,
		"teams_t":teams_t,
		"teams_order_location":teams_order_location,
		"teams_order_team_inv":teams_order_team_inv,
		"jugadores_cooper":jugadores_cooper,
		"jugadores_joshua":jugadores_joshua,
		"jugadores_cooper_joshua":jugadores_cooper_joshua,
		"jugadores_alex_wyatt":jugadores_alex_wyatt
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")