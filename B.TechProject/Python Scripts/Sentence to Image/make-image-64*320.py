import os
import numpy as np
import cv2
import gensim
import sys
from gensim.models import KeyedVectors as kv
#load model read word to vec

# Load Google's pre-trained Word2Vec model.
model_wrdtovec = gensim.models.KeyedVectors.load_word2vec_format('/home/bt3/15CS10019/Tushar/Embeddings/GoogleNews-vectors-negative300.bin', binary=True)
print("model_wordtovec is loaded!")

#load GLOVEMODEL
f = open("/home/bt3/15CS10019/Tushar/Embeddings/glove.6B.300d.txt",'r')
model_glove= {}
for line in f:
	splitLine = line.split()
	word = splitLine[0]
	embedding = np.array([float(val) for val in splitLine[1:]])
	model_glove[word] = embedding
print("model glove is loaded!")


#LOAD READFasttest1
f = open("/home/bt3/15CS10019/Tushar/Embeddings/wiki-text--news-300d-1M.txt",'r')
model_fasttxt = {}
for line in f:
	splitLine = line.split()
	word = splitLine[0]
	embedding = np.array([float(val) for val in splitLine[1:]])
	model_fasttxt[word] = embedding
print("model fasttext is loaded!")
#Write images
direc='/home/bt3/15CS10019/Tushar/Submission/Sentences-train-best'
mylist = os.listdir(direc)

countimg = 0

str_ing="i am a man with honour. it was one of the deadliest attacks in Libya since the end of the 2011 civil war, resulting in a total of at least 40 people killed, although it was not clear how many died in the attack on his residence."

f_image=np.zeros((64,320,3))
print("inilized a image matrix!")
countimg=countimg+1
print(countimg)

#split word and get vectors of length 64*320 from each format in numpy
cnt=0
for word in str_ing.split():
    if word in model_fasttxt:
	 vector1=model_fasttxt[word]
	 #change vector1
	 vector1=vector1-7.1
	 vector1=vector1*4.1
         vector1=vector1+255
	 vec=[0 for i in range(20)]
	 vector1=np.append(vector1,vec)
    else:
	 vector1=[128 for i in range(320)]

    if word in model_glove:
	 vector2=model_glove[word]
	 #chnage vector2
	 vector2=vector2-3.1
	 vector2=vector2*40.36
         vector2=vector2+255
	 vec=[0 for i in range(20)]
	 vector2=np.append(vector2,vec)
    else:
	 vector2=[128 for i in range(320)]

    if word in list(model_wrdtovec.wv.vocab):
	 vector3=model_wrdtovec.wv[word]
	 #chnage vector3
	 vector3=vector3-4.10
	 vector3=vector3*30.96
         vector3=vector3+255
	 vec=[0 for i in range(20)]
	 vector3=np.append(vector3,vec)
    else:
	 vector3=[128 for i in range(320)]
    print("word all three formats",vector1,vector2,vector3)
    for i in range(320):
		f_image[cnt,i,0]=vector1[i]
		f_image[cnt,i,1]=vector2[i]
		f_image[cnt,i,2]=vector3[i]
	    
    cnt=cnt+1
	
#for i in range(0,64) :
#	for j in range(0,320) : 
#		print (f_image[i,j,0],sep=" ")
#	print ('\n')
print(f_image[:,:,0])
cv2.imwrite("new_img1.jpg", f_image)
