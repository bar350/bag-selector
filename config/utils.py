from boardgamegeek.cache import CacheBackend
import requests_cache
from boardgamegeek.exceptions import BGGValueError


class CacheBackendRedis(CacheBackend):
    """ Cache HTTP requests in memory """

    def __init__(self, ttl):
        try:
            int(ttl)
        except ValueError:
            raise BGGValueError
        self.cache = requests_cache.core.CachedSession(backend="redis",
                                                       expire_after=ttl,
                                                       allowable_codes=(200,))
