from django.forms import ModelForm
from .models import GameCategory, GameMechanic, BoardGame, PlayerSuggestion


class GameCategoryForm(ModelForm):
    class Meta:
        model = GameCategory
        fields = '__all__'


class GameMechanicForm(ModelForm):
    class Meta:
        model = GameMechanic
        fields = '__all__'


class BoardGameForm(ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'


class PlayerSuggestionForm(ModelForm):
    class Meta:
        model = PlayerSuggestion
        fields = '__all__'
