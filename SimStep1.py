#!/usr/bin/env python
# -*- coding: utf-8 -*-

import prBubble
import random
import itertools
import json
import os
import re

#baseProteins contains the basic protein templates
baseProteins = {1:[(10, 10), (10, 12), (15, 12), (14, 11)], 2:[(14, 11), (15, 12), (16, 12), (16, 9), (13.5,9)], 3:[(13.5, 9), (16, 9), (16, 6), (13.8, 8)], 4:[(13.8, 8), (16, 6), (7, 6), (7, 7), (12, 7.2)], 5:[(7, 7), (12, 7.2), (10, 10), (10, 12), (7, 12)]}

#matchingTypes contains, for each protein type, the types it can match to merge and form a new protein
matchingTypes = {1:[2,5], 2:[1,3], 3:[2,4], 4:[3,5], 5:[4,1]}

#TODO: 100 is the number of proteins and should be an input parameter
bubble1 = [prBubble.Protein(baseProteins, random.randint(1,5), i, 1) for i in range(100)]

jfile = open('data.json', 'wa')
jfile.write('[')

#TODO 200 steps simulation. This should be an input parameter
for i in range(200):
	print "Run #" + str(i)
	jdump = {}
	jdata=[]
	jdump['run'] = i
	# move each protein	
	for protein in bubble1:		
		#TODO: The movement max values should be an input parameter
		protein.move((random.randint(-10,10), random.randint(-10,10)))
		jdata.append({'id':protein.id, 'coords':protein.coords})
	
	jdump['data'] = jdata
	jdump_string = json.dumps(jdump, sort_keys=True, indent=1) #Human readable
	#jdump_string = json.dumps(jdump)
	jfile.write(jdump_string+',')

	# nearby proteins interacting
	print "Interactions"
	for protA,protB in itertools.combinations(bubble1,2):	
		#TODO: This proximity threshold should be an input parameter
		if protA.dist(protB) < 50: 
			if protB.type in matchingTypes[protA.type]:
				protAIndex = int(re.search('P([0-9]+)$',protA.id).group(1))
				protBIndex = int(re.search('P([0-9]+)$',protB.id).group(1))
				
				print protA.id + " (type " +  str(protA.type) + ")" + " <-> " + protB.id + " (type " +  str(protB.type) + ")"
jfile.seek(-1, os.SEEK_END)
jfile.truncate()
jfile.write(']')
jfile.close()
#print "Original coordinates:\n"
#print bubble1[0].coords
#bubble1[0].move((10,-10))
#print "New coordinates:\n"
#print bubble1[0].coords
