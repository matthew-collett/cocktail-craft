# api/utils/cache.py
from flask_caching import Cache

# Initialize cache
cache = Cache(config={'CACHE_TYPE': 'simple'})
