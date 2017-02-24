from django.views.generic import TemplateView
# from .models import BoardGame
from .utils import get_game_new


class BoardGameDetails(TemplateView):
    template_name = "boardgames/boardgame-detail2.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['boardgame'] = get_game_new(self.kwargs['pk'])
        return ctx
