from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from boardgames.views import VueIndex
from boardgames.views import export_game_list_csv

''' Provide URL for the base view and the exporting as well register 
    the boardgame viewset information '''
urlpatterns = [
	url(r'^boardgames/', include('boardgames.urls')),
    url(r'^export_games$', export_game_list_csv, name='game-export'),
    url(r'', VueIndex.as_view(), name="base"),
]
