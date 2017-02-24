from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Player
from boardgames.utils import get_user_collection
from boardgames.serializers import BoardGameSerializer
from rest_framework.renderers import JSONRenderer


class UserProfile(DetailView):
    template_name = "players/user-profile2.html"
    model = Player
    slug_field = 'bgg_username'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['games'] = get_user_collection(ctx['player'].bgg_username)
        return ctx


class VueIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        boardgames = get_user_collection('bar350')
        serializer = BoardGameSerializer(boardgames, many=True)
        ctx['games'] = JSONRenderer().render(serializer.data)
        return ctx
