#!/usr/bin/env python3
"""
Defines a FIFO cache class.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """Add an item to the cache."""
        if key is None or value is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Delete the oldest item based on insertion order.
            k, _ = self.cache_data.popitem(last=False)
            # Print the discarded kay
            print("DISCARD:", k)

        self.cache_data[key] = value

    def get(self, key):
        """Get an item from the cache."""
        return self.cache_data.get(key, None)
