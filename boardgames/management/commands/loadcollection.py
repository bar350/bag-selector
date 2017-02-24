from django.core.management.base import BaseCommand
from boardgames.utils import upload_user_collection


class Command(BaseCommand):
    help = 'Load a users collection into the database'

    def add_arguments(self, parser):
        parser.add_argument('user_name', nargs='+', type=str)

    def handle(self, *args, **options):
        for user_name in options['user_name']:
            collection = upload_user_collection(user_name)
            if not collection:
                self.stdout.write(
                    self.style.SUCCESS(
                        "User {} Doesn't exists".format(user_name)))
            else:
                self.stdout.write(self.style.SUCCESS(
                    'Successfully uploaded {} collection'.format(user_name)))
