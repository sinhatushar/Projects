import os
import numpy as np
import cv2
import gensim
import sys
from gensim.models import KeyedVectors as kv
#load model read word to vec

# Load Google's pre-trained Word2Vec model.
model_wrdtovec = gensim.models.KeyedVectors.load_word2vec_format('/content/drive/My Drive/Sentence-to-image/GoogleNews-vectors-negative300.bin', binary=True)
print("model_wordtovec is loaded!")

#load GLOVEMODEL
f = open("/content/drive/My Drive/Sentence-to-image/glove.6B.300d.txt",'r')
model_glove= {}
for line in f:
	splitLine = line.split()
	word = splitLine[0]
	embedding = np.array([float(val) for val in splitLine[1:]])
	model_glove[word] = embedding
print("model glove is loaded!")


#LOAD READFasttest1
f = open("/content/drive/My Drive/Sentence-to-image/wiki-news-300d-1M.vec",'r')
model_fasttxt = {}
for line in f:
	splitLine = line.split()
	word = splitLine[0]
	embedding = np.array([float(val) for val in splitLine[1:]])
	model_fasttxt[word] = embedding
print("model fasttext is loaded!")


direc='/content/drive/My Drive/Sentence-to-image/Sentences-train-final'
mylist = os.listdir(direc)

f_image=np.zeros((416,416,3))
print("inilized a image matrix!")
countimg = 0


#split word and get vectors of length 416*416 from each format in numpy

for filename in mylist:
	path = direc + '/'+ filename
	f1 = open(path,"r")
	content1 = f1.readlines() 
	sentence = content1[0]
	sentence = sentence.strip()
	str_ing = sentence
	cnt = 0

	for word in str_ing.split():

		if word in model_fasttxt:
			vector1=model_fasttxt[word]	
			vector1=vector1-7.1
			vector1=vector1*4.1
			vector1=vector1+255
		else:
			vector1=[128 for i in range(300)]


		if word in model_glove:
			vector2=model_glove[word]
			vector2=vector2-3.1	
			vector2=vector2*40.36
			vector2=vector2+255
		else:
			vector2=[128 for i in range(300)]
		

		if word in list(model_wrdtovec.wv.vocab):
			vector3=model_wrdtovec.wv[word]
			vector3=vector3-4.10
			vector3=vector3*30.96
			vector3=vector3+255 
		else:
			vector3=[128 for i in range(300)]

		for i in range(300):
			f_image[6*cnt,i,0]=vector1[i]
			f_image[6*cnt,i,1]=vector2[i]
			f_image[6*cnt,i,2]=vector3[i]
			
			f_image[6*cnt+1,i,0]=vector1[i]
			f_image[6*cnt+1,i,1]=vector2[i]
			f_image[6*cnt+1,i,2]=vector3[i]

			f_image[6*cnt+2,i,0]=vector1[i]
			f_image[6*cnt+2,i,1]=vector2[i]
			f_image[6*cnt+2,i,2]=vector3[i]

			f_image[6*cnt+3,i,0]=vector1[i]
			f_image[6*cnt+3,i,1]=vector2[i]
			f_image[6*cnt+3,i,2]=vector3[i]

			f_image[6*cnt+4,i,0]=vector1[i]
			f_image[6*cnt+4,i,1]=vector2[i]
			f_image[6*cnt+4,i,2]=vector3[i]

			f_image[6*cnt+5,i,0]=vector1[i]
			f_image[6*cnt+5,i,1]=vector2[i]
			f_image[6*cnt+5,i,2]=vector3[i]

		cnt=cnt+1

	countimg=countimg+1
	print(countimg)

	path2 = filename[0:-4]
	path2 += ".jpg"   
	cv2.imwrite(path2, f_image)
	
#for i in range(0,64) :
#	for j in range(0,320) : 
#		print (f_image[i,j,0],sep=" ")
#	print ('\n')
#print(f_image[:,:,0])

