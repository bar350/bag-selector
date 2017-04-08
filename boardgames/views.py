from django.views.generic import TemplateView
from .utils import get_game_new
import csv

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .utils import get_games


''' Base view this views is only responsible for loading the template 
    this template then runs the vue.js code responsible for the application '''
class VueIndex(TemplateView):
    template_name = 'indexPy.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


''' Export view which is called as a POST route, 
    this view requires a list of game ids to be passed in. 
    This view will then output a CSV to the caller with the informaiton
    on the supplied games '''
def export_game_list_csv(request):
    if request.method != "POST":
    	return Response({"Must Pass in a List of Game IDs"},
                          status=status.HTTP_400_BAD_REQUEST)

    game_ids = request.POST.getlist('games')
    games = get_games(game_ids)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="games.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Rating', 'Weight', 'Player Count', 
    	'Playing Time', 'Categories', 'Mechanics',
    	'Description'])

    for game in games:
    	playing_time = str(game.min_playing_time)
    	if(game.max_playing_time and game.max_playing_time != game.min_playing_time):
    		playing_time += ' - ' + str(game.max_playing_time)

    	player_count = str(game.min_players)
    	if(game.max_players and game.max_players != game.min_players):
    		player_count += ' - ' + str(game.max_players)

    	game_row = ( game.name, 
    		game.rating_bayes_average,
			game.rating_average_weight,
			playing_time,
			player_count,
			', '.join(game.categories),
			', '.join(game.mechanics),
			game.description)
    	writer.writerow(game_row)

    return response