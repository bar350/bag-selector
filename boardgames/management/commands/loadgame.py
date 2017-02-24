from django.core.management.base import BaseCommand
from boardgames.utils import add_game
from boardgames.models import BoardGame


class Command(BaseCommand):
    help = 'Load a BoadGame into the database'

    def add_arguments(self, parser):
        parser.add_argument('game_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for game_id in options['game_id']:
            if not BoardGame.objects.filter(bgg_id=game_id).exists():
                game = add_game(game_id)

                self.stdout.write(self.style.SUCCESS(
                    'Successfully added game "%s"' % game.name))
            else:
                self.stdout.write(self.style.SUCCESS(
                    'Game Already Exists in the Database "%s"' % game_id))
