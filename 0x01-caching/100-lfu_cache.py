#!/usr/bin/python3
"""LFU caching module"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    This class has a LFU caching system that inherits from
    BaseCaching
    """

    def __init__(self):
        """
        Initialize the LFU caching system
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def arrange(self, mru_key):
        """Arranges items in this cache based on the most
        recently used item to the least used
        """
        positions = []
        mru_freq = 0
        mru_pos = 0
        ins = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(positions) == 0:
                positions.append(i)
            elif key_freq[1] < self.keys_freq[positions[-1]][1]:
                positions.append(i)
        positions.reverse()
        for pos in positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins, [mru_key, mru_freq])

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.arrange(key)
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.arrange(key)
