
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:24:08 2018

@author: TS
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wikipedia

with open("/home/tushar/Desktop/BTP/dbpedia50/entities1.txt") as f:
	    con = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
con = [x.strip() for x in con] 

k=0

for j in con:
	try: 
		path='/home/tushar/Desktop/BTP/Crawl2/'
		path+=j
		path+='.txt'
	##wikiurl='https://en.wikipedia.org/wiki/Florence Ballard'
		WikiSearch = j
		p = wikipedia.summary(WikiSearch)
	#print(p.content[2])
		content=''
		
		for i in p:
			try:
				content=content+str(i)
			except:
				pass

		ContentFile = open(path,'w')
		ContentFile.write(content)
		ContentFile.close()
		k=k+1
		#print(k)
	except:
		pass