#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
import Stats

class TestStats(unittest.TestCase):
    def setUp(self):
        Stats._drop_stats_controller()

    def test_initial_results(self):
        self.assertEqual({}, Stats.results())

    def test_increment(self):
        Stats.increment("A resolution")
        Stats.increment("Another one")
        Stats.increment("A resolution")

        self.assertItemsEqual({"A resolution": 2, "Another one": 1}, Stats.results())

    def test_increment_with_step(self):
        Stats.increment("A resolution", 1)
        Stats.increment("Another one", 2)
        Stats.increment("A resolution", 3)

        self.assertItemsEqual({"A resolution": 4, "Another one": 2}, Stats.results())

if __name__ == '__main__':
    unittest.main()

