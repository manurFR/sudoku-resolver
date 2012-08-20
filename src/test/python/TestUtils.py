#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
from Grid import SIZE
from NakedSingleResolution import NakedSingleResolution

def prepareRemainingCandidates(grid):
    logging.disable(logging.WARNING)
    nakedSingleResolution = NakedSingleResolution()
    for x in range(SIZE):
        for y in range(SIZE):
            nakedSingleResolution.horizontal_naked_single(grid, x, y)
            nakedSingleResolution.vertical_naked_single(grid, x, y)
            nakedSingleResolution.block_naked_single(grid, x, y)
    logging.disable(logging.NOTSET)

