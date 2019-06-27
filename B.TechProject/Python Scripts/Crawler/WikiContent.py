
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:24:08 2018

@author: TS
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wikipedia

with open("/home/tushar/Desktop/BTP/dbpedia50/entities.txt") as f:
	    con = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
con = [x.strip() for x in con] 



for j in con:
	try: 
		path='/home/tushar/Desktop/BTP/Crawl/'
		path+=j
		path+='.txt'
	##wikiurl='https://en.wikipedia.org/wiki/Florence Ballard'
		WikiSearch = j
		p = wikipedia.page(WikiSearch)
	#print(p.content[2])
		content=''
		for i in p.title:
			try:
				content=content+str(i)
			except:
				pass
		content = content + '\n\n'		
		for i in p.content:
			try:
				content=content+str(i)
			except:
				pass
		content=content.split('==')[0]
		ContentFile = open(path,'w')
		ContentFile.write(content)
		ContentFile.close()
	except:
		pass