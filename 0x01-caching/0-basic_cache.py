#!/usr/bin/env python3
"""
Basic caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ This class Inherits from BaseCaching and represents a caching system
    """

    def put(self, key, item):
        """ Add an item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
