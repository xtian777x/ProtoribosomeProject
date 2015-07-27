#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapely.geometry import Polygon
import random

#general function to move a vector
def moveVector(point, distance):
	return tuple(map(sum,zip(point,distance)))

#Defining a protein
#ThOrigin: The protein will be shifted (random(-ThOrigin,ThOrigin), random(-ThOrigin,ThOrigin)) from its original coordinates.

class Protein:
	def __init__(self, baseproteins, type, ThOrigin=100):		
		self.type = type
		self.ThOrigin = ThOrigin
		self.originshift = (random.uniform(-self.ThOrigin, self.ThOrigin), random.uniform(-self.ThOrigin, self.ThOrigin))
		self.coords = [moveVector(x, self.originshift) for x in baseproteins[type]]

	def move(self, vector):
		self.coords = [moveVector(x, vector) for x in self.coords]

#baseProteins contains the basic protein shapes
baseProteins = {1:[(10, 10), (10, 12), (15, 12), (14, 11)], 2:[(14, 11), (15, 12), (16, 12), (16, 9), (13.5,9)], 3:[(13.5, 9), (16, 9), (16, 6), (13.8, 8)], 4:[(13.8, 8), (16, 6), (7, 6), (7, 7), (12, 7.2)], 5:[(7, 7), (12, 7.2), (10, 10), (10, 12), (7, 12)]}

bubble1 = [Protein(baseProteins, random.randint(1,5)) for i in range(10)]
print "Original coordinates:\n"
print bubble1[0].coords
bubble1[0].move((10,-10))
print "New coordinates:\n"
print bubble1[0].coords
