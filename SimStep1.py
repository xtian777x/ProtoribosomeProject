#!/usr/bin/env python
# -*- coding: utf-8 -*-

import prBubble
import random

#baseProteins contains the basic protein templates
baseProteins = {1:[(10, 10), (10, 12), (15, 12), (14, 11)], 2:[(14, 11), (15, 12), (16, 12), (16, 9), (13.5,9)], 3:[(13.5, 9), (16, 9), (16, 6), (13.8, 8)], 4:[(13.8, 8), (16, 6), (7, 6), (7, 7), (12, 7.2)], 5:[(7, 7), (12, 7.2), (10, 10), (10, 12), (7, 12)]}

bubble1 = [prBubble.Protein(baseProteins, random.randint(1,5)) for i in range(10)]
print "Original coordinates:\n"
print bubble1[0].coords
bubble1[0].move((10,-10))
print "New coordinates:\n"
print bubble1[0].coords
