#!/usr/bin/env python
import unittest
from lru import LRUCache

class TestLRUFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_cache(self):
        cache = LRUCache(3)
        cache['a'] = 1
        cache['b'] = 2
        cache['c'] = 3
        self.assertEqual(len(cache.data), 3)
        self.assertEqual(cache['a'], 1)
        self.assertEqual(cache['b'], 2)
        self.assertEqual(cache['c'], 3)

    def test_lru_func(self):
        cache = LRUCache(3)
        self.assertEqual(cache.lru(), None)
        cache['a'] = 1
        cache['b'] = 2
        cache['c'] = 3
        self.assertEqual(cache.lru(), ('a', 1))
        cache['a']
        self.assertEqual(cache.lru(), ('b', 2))
        cache['b']
        self.assertEqual(cache.lru(), ('c', 3))

    def test_contains(self):
        cache = LRUCache(3)
        cache['a'] = 1
        self.assertTrue('a' in cache)
        self.assertTrue('z' not in cache)

    def test_overwrite(self):
        cache = LRUCache(3)
        cache['a'] = 1
        cache['b'] = 2
        cache['c'] = 3
        cache['d'] = 4
        self.assertEqual(len(cache.data), 3)
        self.assertTrue('a' not in cache)
        self.assertTrue('b' in cache)
        self.assertTrue('c' in cache)
        self.assertTrue('d' in cache)
        self.assertEqual(cache.lru(), ('b', 2))
        cache['b']
        cache['e'] = 5
        self.assertEqual(len(cache.data), 3)
        self.assertTrue('c' not in cache)
        self.assertTrue('b' in cache)
        self.assertTrue('d' in cache)
        self.assertTrue('e' in cache)

if __name__ == '__main__':
    unittest.main()

