# NLP_Project
Project work given as part of NLP course.

Link to Dataset: https://figshare.com/articles/InSciOut/903704

Scientific misinformation detection in news media

Step 1:Text Preprocessing:

Given dataset contains Press releases and News articles in docs format therefore all docs file were converted into txt format as NLTK tools can be easily applied only txt format files. Then text cleaning was done in which first text is tokenized and all punctuation marks and stop words were removed. Further stemming is done to stem ‘snowball’ stammers is used. This whole process is done for news articles as well as for press releases. Further cleaned corpus were created for Press releases and news articles separately.

Step2: Maxentropy model Implementation.

For implementing maxent model first document term matrix is required to be created. We have used 298 high emotion words as vocabulary which is used for creating document term matrix. For each document a vector was created which contain frequency of these high emotion words therefore each document is represented as 298*1 vector. Now, using these document term matrix maxent model is trained and tested. For training model we have used 70% of news articles as training data and 30% data as test data.

Step 3: Document to vector conversion :

For converting documents into vectors we first created vocabulary containing all press releases and news articles. Then gensim model is used for converting each document into a 300*1 vector. Then to test relationship between news articles and press releases we computed cosine similarity of news article and corresponding press release. Our hypothesis was that for exaggerated news articles cosine similarity will be less as compared to non-exaggerated articles. Working on that we have observed that hypothesis seems to be true that’s why we proceed to consider these doc2vec vectors as features for training our supervised and unsupervised learning models.

Step 4 :Supervised Learning Models:

Further for training supervised learning models we have used our 70% news articles as training dataset and rest 30% for test dataset. Now many supervised learning Classifiers were implemented including Logistic regression, SVM, XGBoost, Bagging Classifiers, Random Forest, KNN etc. We implemented our classifiers on two sets of features one set contains only news articles vectors as features and another set which contain concatenated vectors of news article and corresponding press release.

Step 5:Unsupervised Learning Approach :

We uses clustering algorithms like K-Means, Agglomerative, DBSCAN, HDBSCAN etc.Among them purity of K-Means and Agglomerative observed to be best.
