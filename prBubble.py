from shapely.geometry import Polygon
import random

#general function to move a vector
def moveVector(point, distance):
	return tuple(map(sum,zip(point,distance)))

#Defining a protein
#ThOrigin: The protein will be shifted (random(-ThOrigin,ThOrigin), random(-ThOrigin,ThOrigin)) from its original coordinates.
#type: type of template protein
#ip: protein index used to create the ID
#ib: bubble index used to create the ID
#nature: could be O (original), H (hybrid) or D (dissociated)
#status: 1:active 0:inactive. The protein is inactive when it merged with another and one is discarded
#baseTemplate: coordinates of the base protein(s) forming this protein
# We should have a 'structure' property which would be a list of joined proteins 

class Protein:
	def __init__(self, baseproteins, type, ip, ib, ThOrigin=100):		
		self.type = type
		self.id = "B" + str(ib) + "T" + str(type) + "P" + str(ip)
		#self.ThOrigin = ThOrigin #should be removed from here
		self.originshift = (random.uniform(-ThOrigin, ThOrigin), random.uniform(-ThOrigin, ThOrigin))
		self.coords = [moveVector(x, self.originshift) for x in baseproteins[type]]
		self.nature = "O"
		self.status = 1
		self.baseTemplate = []

	#Moving a whole protein structure
	def move(self, vector):
		self.coords = [moveVector(x, vector) for x in self.coords]

	def dist(self, element):
		return Polygon(self.coords).distance(Polygon(element.coords))