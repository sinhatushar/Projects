import os  

direc='/home/tushar/Desktop/Imp Files/BTP/Submission/Sample1OpenIE'

mylist = os.listdir(direc)

for filename in mylist:
	path = direc + '/'+ filename  
	f = open(path,"r")
	content = f.readlines()
	sentence1=''
	for line in content:
		mark=0
		sentence1=''
		line = line.strip() 
		if len(line.strip()) == 0 :
			break
		sentence = line.split('\t')
		if float(sentence[0]) > 0.9 :
			sentence1=sentence
			mark=1
			break

	if len(sentence1)==0 :
		f1 = open("/home/tushar/Desktop/Imp Files/BTP/Submission/Selected-triple/"+filename,"w")
		f1.write(sentence1)
		f1.close()
		f.close()	
	elif len(line.strip())>0 :
		s = sentence1[1:]
		s = '\n'.join(s)
		f1 = open("/home/tushar/Desktop/Imp Files/BTP/Submission/Selected-triple/"+filename,"w")
		f1.write(s)
		f1.close()
		f.close()

	

