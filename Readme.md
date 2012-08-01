# Least Recently Used (LRU) Cache

This is a Python 2 implementation of a Least Recently Used Cache.

## Usage

    from lru import LRUCache
    
    cache = LRUCache(3)     # Create a cache for 3 items
    cache['a'] = 1          # Add items
    cache['b'] = 2
    cache['c'] = 3
    
    cache.lru()             # Returns ('a', 1)
    
    cache['b']              # Get items
    cache['a']
    cache['c']
    
    cache.lru()             # Now, 'b' is the LRU
    
    cache['d'] = 4          # Overwrite 'b' with 'd'
    
    if 'b' not in cache:
        print "b has been overwritten"
    
    print cache.keys()      # ['a', 'c', 'd']
    

### Requirements

* Python 2.7 (requires collections.OrderedDict)

### Unit Tests

Run the unit tests for the LRUCache

    ./lru_test


