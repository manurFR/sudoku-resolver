#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
import Stats

class TestStats(unittest.TestCase):
    def setUp(self):
        Stats._drop_stats_controller()

    def test_resultat_initiaux(self):
        self.assertEqual({}, Stats.results())

    def test_increment(self):
        Stats.increment("Une resolution")
        Stats.increment("Une autre")
        Stats.increment("Une resolution")

        self.assertItemsEqual({"Une resolution": 2, "Une autre": 1}, Stats.results())

if __name__ == '__main__':
    unittest.main()

