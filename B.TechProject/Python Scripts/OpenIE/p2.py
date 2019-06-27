import subprocess
import os


#subprocess.call("cd /home/tushar/Desktop/BTP/stanford-corenlp-full-2018-10-05/",shell= True)

os.chdir("/home/tushar/Desktop/BTP/stanford-corenlp-full-2018-10-05/")
cwd = os.getcwd()
print(cwd)


from os import listdir

path =  "/home/tushar/Desktop/BTP/Crawl2/Output/"
path2 = "/home/tushar/Desktop/BTP/Crawl2/Output1/"

files = listdir(path)

for file in files:
	path1 = path + file
	path3 = path2 + file
	subprocess.call(' java -mx4g -cp "*" edu.stanford.nlp.naturalli.OpenIE  '+path1+' > '+path3,shell= True)
