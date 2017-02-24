from django.contrib import admin
from .models import GameCategory, GameMechanic, BoardGame, PlayerSuggestion
# Register your models here.

admin.site.register(GameCategory)
admin.site.register(GameMechanic)
admin.site.register(BoardGame)
admin.site.register(PlayerSuggestion)
