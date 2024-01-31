#!/usr/bin/env python3
""" MRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    This class represents a caching system that uses
    the MRU algorithm and inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize the MRUCache instance
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item using the MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.queue.pop()
                    del self.cache_data[discarded_key]
                    print("DISCARD:", discarded_key)
            else:
                if key in self.queue:
                    self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
