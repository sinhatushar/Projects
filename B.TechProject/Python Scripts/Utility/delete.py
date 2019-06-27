import os  

path='/home/tushar/Desktop/Submission/1747-train-images-416*416' 

mylist1 = os.listdir(path) 

path='/home/tushar/Desktop/Submission/1976-VOC-refined-416*416-yolo3-debug' 
	
mylist = os.listdir(path)  

for j in mylist:  
	mark=0  
	for  i in mylist1:  
		t1=i[0:-4]
		t2=j[0:-4]
		if t1==t2 :
			mark=1
			break
	if mark==0 :
		os.remove(path+'/'+j)







