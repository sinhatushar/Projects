from nltk.tokenize import sent_tokenize

from os import listdir
path =  "/home/tushar/Desktop/BTP/Crawl2/First/"
path2 = "/home/tushar/Desktop/BTP/Crawl2/Output/"

files = listdir(path)

for file in files:
	path1 = path + file
	f  = open(path1,"r")
	tokens = sent_tokenize(f.read())
	f.close()
	for i in range(len(tokens)):
		path3 = path2+file[:-4]+"_"+str(i+1)+".txt"
		file1 = open(path3, "w")
		file1.write(tokens[i])
		file1.close()




