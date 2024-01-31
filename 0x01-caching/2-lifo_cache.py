#!/usr/bin/env python3
""" LIFO caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    This class gives a caching system that use the
    LIFO method and inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item using the LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.queue.pop()
                    del self.cache_data[discarded_key]
                    print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Return an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
