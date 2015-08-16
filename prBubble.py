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
		#self.ThOrigin = ThOrigin #should be removed from here
		self.originshift = (random.uniform(-ThOrigin, ThOrigin), random.uniform(-ThOrigin, ThOrigin))
		self.coords = [moveVector(x, self.originshift) for x in baseproteins[type]]

	#Moving a whole protein structure
	def move(self, vector):
		self.coords = [moveVector(x, vector) for x in self.coords]

	def dist(self, element):
		return Polygon(self.coords).distance(Polygon(element.coords))