from boardgamegeek import BGGClient
from django.core.cache import cache
from config.utils import CacheBackendRedis
import json


class BoardGameExtension(object):

    def __init__(self, bg):
        self._bg = bg

    def __getattr__(self, var):
        # for non altered functions, properties
        # just do what _bg would do
        return self._bg.__getattribute__(var)

    def get_best_count(self):
        best_list = []
        for suggestion in self.player_suggestions:
            total = suggestion.best + suggestion.recommended + suggestion.not_recommended
            if total != 0 and (suggestion.best / total) * 100 > 50:
                best_list.append(suggestion.player_count)
        best_list.sort()
        return ", ".join(best_list)

    def get_recommended_count(self):
        best_list = []
        for suggestion in self.player_suggestions:
            total = suggestion.best + suggestion.recommended + suggestion.not_recommended
            if (total != 0 and
                    ((suggestion.recommended + suggestion.best) / total) * 100 > 50):
                best_list.append(suggestion.player_count)
        best_list.sort()
        return ", ".join(best_list)

    def jsonify(self):
        return json.dumps(self._bg._data)


def createBGGClient():
    # redis_backend = CacheBackendRedis(ttl=2592000)
    # bgg = BGGClient(cache=redis_backend)
    bgg = BGGClient()
    return bgg


def get_user_from_bgg(user_name):
    bgg = createBGGClient()
    collection = bgg.collection(user_name, own=True)
    return collection


def get_user_collection(user_name):
    collection = cache.get('collection_' + user_name, None)

    if collection is None:
        collection = get_user_from_bgg(user_name)
        cache.add('collection_' + user_name, collection)

    if collection is None:
        return None

    owned_games = []
    for game in collection.items:
        if game.owned:
            owned_games.append(str(game.id))
    games_cached = cache.get_many(['game_' + game_id for game_id in owned_games])

    lookup_games = list(set(owned_games) - set([game_id[5:]
                                                for game_id in games_cached.keys()]))

    games_returned = []
    if lookup_games:
        bgg = createBGGClient()
        for i in range(0, len(lookup_games), 50):
            new_return = bgg.game_list(game_id_list=lookup_games[i:i + 50])
            games_returned = games_returned + new_return

        for returned in games_returned:
            cache.add('game_' + str(returned.id), returned)

    games = []
    for game in games_returned + list(games_cached.values()):
        games.append(BoardGameExtension(game))

    games.sort(key=lambda k: k.name)
    return games


def get_game_from_bgg(game_id):
    bgg = createBGGClient()
    return bgg.game(game_id=game_id)


def get_game_new(game_id):
    game = cache.get('game_' + game_id, None)
    if game is None:
        game = get_game_from_bgg(game_id)
        cache.add(game_id, game)

    return BoardGameExtension(game)
