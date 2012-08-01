#!/usr/bin/env python

from collections import OrderedDict

class LRUCache(object):
    """
    LRU Cache based on a Python OrderedDict

    The OrderedDict is a dict that maintains a doubly linked list which saves the order
    that keys are inserted.  When a cache item is accessed, the item is popped
    and reinserted in the OrderedDict so that the recently used order is preserved.

    The internal OrderedDict is accessible as `self.data`

    OrderedDict references
    http://docs.python.org/library/collections.html#collections.OrderedDict
    http://hg.python.org/cpython/file/70274d53c1dd/Lib/collections.py
    """
    def __init__(self, size):
        self.size = size
        self.data = OrderedDict()

    def __getitem__(self, key):
        # pop and reinsert so that this item is now last
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def __setitem__(self, key, value):
        if key in self.data:
            self.data.pop(key)
        elif len(self.data) == self.size:
            # cache full: delete the least recently used item (first item)
            self.data.popitem(last=False)
        self.data[key] = value

    def __contains__(self, item):
        return item in self.data

    def __str__(self):
        return "LRUCache (size={size}, length={length}) {data}".format(
                size=self.size, length=len(self.data), data=str(self.data))

    def lru(self):
        """
        Returns the least recently used item's (key, value) tuple
        """
        if len(self.data) == 0:
            return None
        key = self.data.iterkeys().next()
        return (key, self.data[key])

    def keys(self):
        """
        Returns the keys in the cache ordered from least recently used to 
        most recently used
        """
        return self.data.keys()


if __name__ == "__main__":
    # Debug code
    cache = LRUCache(3)
    cache['a'] = 1
    cache['b'] = 2
    cache['c'] = 3
    print cache.lru()
    cache['d'] = 4
    print cache.lru()

    if 'a' not in cache:
        print "'a' not in cache. It got overwritten because it was the least recently used item"
    else:
        print "something went wrong"

    print cache.keys()
    print cache.lru()

    for key,value in cache.data.iteritems():
        print "cache[{key}] = {value}".format(key=key, value=value)

    print cache
