from django.forms import ModelForm
from .models import GameGroup, Player


class GameGroupForm(ModelForm):
    class Meta:
        model = GameGroup
        fields = '__all__'


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
