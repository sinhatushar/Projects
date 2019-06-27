import os  

direc='/home/tushar/Desktop/Imp Files/BTP/Submission/Sample1SentenceSplit'

mylist = os.listdir(direc)

for filename in mylist:
	path = direc + '/'+ filename  
	f = open(path,"r")
	content = f.readlines()

	for line in content:
		line = line.replace(',', '')
		line = line.replace('.','')
		f1 = open("/home/tushar/Desktop/Imp Files/BTP/Submission/Sentences-train/"+filename,"w")
		f1.write(line)
		f1.close()
		f.close()

	

