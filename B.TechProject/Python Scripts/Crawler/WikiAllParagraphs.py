# -*- coding: utf-8 -*-
"""
Created on Mon Dec 9 22:24:08 2018

@author: TS
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
path='/home/tushar/Desktop/BTP/allparagraphs.txt' ####Enter the path to your file here
wiki_url='https://en.wikipedia.org/wiki/Narendra_Modi' #####Enter the wiki url here
source_code = requests.get(wiki_url).text
soup = BeautifulSoup(source_code,'html.parser')
a=soup.findAll('p')
allparagraphs=''
for i in a:
	allparagraphs=allparagraphs+i.text+'\n'
	#print(i.text)
#print(allparagraphs)
allparagraphsFile = open(path,'w')
allparagraphsFile.write(wiki_url[30:]+'\n')

allparagraphsFile.write(allparagraphs+'\n\n--------------------------------------')
allparagraphsFile.close()
