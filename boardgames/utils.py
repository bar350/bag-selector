from boardgamegeek import BGGClient
from boardgamegeek.exceptions import BGGItemNotFoundError, BGGApiRetryError
from django.core.cache import cache
from config.utils import CacheBackendRedis
import json

def createBGGClient():
    ''' Abstract the creation of the BGG Client, 
        so that if any changes need to be they can be made in one place '''
    # redis_backend = CacheBackendRedis(ttl=2592000)
    # bgg = BGGClient(cache=redis_backend)
    bgg = BGGClient()
    return bgg


def get_user_from_bgg(user_name):
    ''' Abstract the user collection retrival from bgg '''
    bgg = createBGGClient()
    try:
        collection = bgg.collection(user_name)
    except (BGGItemNotFoundError, BGGApiRetryError) as err:
        raise err

    return collection


def get_games(owned_games):
    ''' Take a list of games as input
        Check the cache for the games by id, return those that are available in the cache
        For any that are not available in the cache create a connection to bgg 
        Retrieve 50 games at a time from BGG. Then return those games '''
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
        games.append(game)

    games.sort(key=lambda k: k.name)
    return games

def get_user_collection(user_name):
    ''' Given a username check the cache for that users collection information
        If the Collection is not found connect to BGG and retrieve the users connection
        Then call get_games to retireve the users owned games. 
        Lastly return the collection and the games '''
    collection = cache.get('collection_' + user_name, None)

    if collection is None:
        try:
            collection = get_user_from_bgg(user_name)
        except (BGGItemNotFoundError, BGGApiRetryError) as err:
            raise err
        cache.add('collection_' + user_name, collection)

    if collection is None:
        return None

    owned_games = []
    for game in collection.items:
        if game.owned:
            owned_games.append(str(game.id))
    
    games = get_games(owned_games)
    return (collection, games)


def get_game_from_bgg(game_id):
    ''' Retrieve a single game from BoardGameGeek '''
    bgg = createBGGClient()
    return bgg.game(game_id=game_id)


def get_game_new(game_id):
    ''' Check the cache for a given game id 
        If it doesn't exist call get_game_from_bgg
        Return the game information '''
    game = cache.get('game_' + game_id, None)
    if game is None:
        game = get_game_from_bgg(game_id)
        cache.add(game_id, game)

    return game
