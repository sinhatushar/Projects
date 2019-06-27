# -*- coding: utf-8 -*-
"""
Created on Mon Dec 9 22:24:08 2018

@author: TS
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
path='/home/tushar/Desktop/BTP/Summary.txt' ####Enter the path to your file here
wiki_url='https://en.wikipedia.org/wiki/Pablo_Gaglianone' #####Enter the wiki url here
source_code = requests.get(wiki_url).text
soup = BeautifulSoup(source_code,'html.parser')
t=soup.find('div',{'id':'bodyContent'})
t1=t.find('div',{'class':'mw-parser-output'})
t2=str(t1)
#print(type(t2))
ind1=t2.find('<p')
#print(ind1)
#print(t2[ind1:ind1+10])
flag=1
no_of_ps=0
ptext=''
i=0		

while flag==1:
	ind1=t2[i:].find('<p')
	if(ind1==-1):
		break
	else:
		if((t2[ind1:].find('<p class="mw-empty-elt">'))!=(-1)):
			ind2=t2[ind1:].find('<p class="mw-empty-elt">')+ind1
			#print(ind2)
			ind3=t2[ind2+10:].find('<p')+ind2+10
			#print(t2[ind3:ind3+100])
			ind4=t2[ind3+5:].find('</p>')+ind3+5
			#print(t2[ind3:ind4+4])
			ptext=ptext+t2[ind3:ind4+4]
			while flag==1:
				ind5=t2[ind4+4:].find('<')+ind4+4
				if(t2[ind5+1]!='p'):
					break
				#print(t2[ind5+1])	
				ind2=ind5
				ind3=t2[ind2:].find('<p')+ind2
				#print(t2[ind3:ind3+100])
				ind4=t2[ind3+5:].find('</p>')+ind3+5
				#print(t2[ind3:ind4+4])
				ptext=ptext+t2[ind3:ind4+4]
			flag=2
#print(ptext)
soup = BeautifulSoup(ptext,'html.parser')
plist=soup.findAll('p')
Summary=''
for i in plist:
	Summary=Summary+i.text+'\n'
	#print(i.text)
#print(len(Summary))
SummaryFile = open(path,'w')
SummaryFile.write(wiki_url[30:])
SummaryFile.write('\n'+'\n')
SummaryFile.write(Summary)
SummaryFile.write('\n\n----------------------------------------------------------------------------------------------')
SummaryFile.close()
if(len(Summary)<25):
	t3=str(t)
	ind9=t3.find('div class="toc')
	#print(ind9)
	soup=BeautifulSoup(t3[:ind9], 'html.parser')
	plist=soup.findAll('p')
	Summary=''
	for i in plist:
		Summary=Summary+i.text+'\n'
	#print(i.text)
	#print(len(Summary))
	SummaryFile = open(path,'w')
	SummaryFile.write(wiki_url[30:])
	SummaryFile.write('\n'+'\n')
	SummaryFile.write(Summary)
	SummaryFile.write('\n\n----------------------------------------------------------------------------------------------')
	SummaryFile.close()