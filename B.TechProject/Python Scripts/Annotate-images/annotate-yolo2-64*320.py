import os  

direc1 = '/home/tushar/Desktop/Submission/Sample1SentenceSplit'
direc2 = '/home/tushar/Desktop/Submission/Selected-triple'

mylist1 = os.listdir(direc1)

xminsub=0
xmaxsub=315
xminrel=0
xmaxrel=315
xminobj=0
xmaxobj=315

yminsub=-1
yminsub=-1
yminrel=-1
ymaxrel=-1
yminobj=-1
ymaxobj=-1

emptycount=0

for filename in mylist1:
	path1 = direc1 + '/'+ filename
	path2 = direc2 + '/'+ filename
	f1 = open(path1,"r")
	content1 = f1.readlines() 
	sentence = content1[0]
	sentence = sentence.strip()

	
	f2 = open(path2,"r")
	content2 = f2.readlines()
	if (len(content2) == 0) :
		emptycount=emptycount+1
		continue
	else :
		sub = content2[0].strip()
		rel = content2[1].strip()
		obj = content2[2].strip()


		#Finding position for subject
		possub = sentence.find(sub) 
		if (possub==0) :
			yminsub = 0
			ymaxsub = yminsub+len(sub.split())
		elif (possub==-1) :			
			sublist=sub.split()
			subfirstword=sublist[0]
			firstwordpos=sentence.find(subfirstword)
			auxstr=sentence[0:firstwordpos-1]
			yminsub=len(auxstr.split())
			ymaxsub=yminsub+len(sub.split())
		else :
			auxstr = sentence[0:possub-1]
			yminsub = len(auxstr.split())
			ymaxsub = yminsub+len(sub.split())


		#Finding position for relation
		posrel = sentence.find(rel) 
		if (posrel==0) :
			yminrel = 0
			ymaxrel = yminrel+len(rel.split())
		elif (posrel==-1) :			
			rellist=rel.split()
			relfirstword=rellist[0]
			firstwordpos=sentence.find(relfirstword)
			auxstr=sentence[0:firstwordpos-1]
			yminrel=len(auxstr.split())
			ymaxrel=yminrel+len(rel.split())
		else :
			auxstr = sentence[0:posrel-1]
			yminrel = len(auxstr.split())
			ymaxrel = yminrel+len(rel.split())


		#Finding position for object
		posobj = sentence.find(obj) 
		if (posobj==0) :
			yminobj = 0
			ymaxobj = yminobj+len(obj.split())
		elif (posobj==-1) :			
			objlist=obj.split()
			objfirstword=objlist[0]
			firstwordpos=sentence.find(objfirstword)
			auxstr=sentence[0:firstwordpos-1]
			yminobj=len(auxstr.split())
			ymaxobj=yminobj+len(obj.split())
		else :
			auxstr = sentence[0:posobj-1]
			yminobj = len(auxstr.split())
			ymaxobj = yminobj+len(obj.split())


		finresult = str(xminsub)+', '+str(yminsub)+', '+str(xmaxsub)+', '+str(ymaxsub)+', '+'subject, '+str(xminrel)+', '+str(yminrel)+', '+str(xmaxrel)+', '+str(ymaxrel)+', '+'relation, '+str(xminobj)+', '+str(yminobj)+', '+str(xmaxobj)+', '+str(ymaxobj)+', '+'object'
		f3 = open("/home/tushar/Desktop/Submission/VOC1/"+filename,"w")
		f3.write(finresult)
		f3.close()
		f1.close()
		f2.close()

print(emptycount)











	
