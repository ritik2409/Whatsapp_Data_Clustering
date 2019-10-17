# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:18:30 2019

@author: Ritik
"""
import numpy as np
from sklearn.cluster import KMeans
import datetime
import os
import cleaning
from config import *

clustered_data = []

#cluster function for clustering
#takes number of clusters and google pretrained model
def clusters(k,model):
    #Generate a numpy array for clustering using gensim google pretrained model
    final_ls = []
    for sentence in cleaning.lowered_data:
        ls = []
        for word in sentence:
            if word in model.vocab:
                ls.append(model[word])
        ls = np.array(ls)
        final_ls.append(numpymean(ls))           
    np_ls = np.array(final_ls)
    clustering(np_ls,k)
    return

#Function to write to text file from list of clustered_data
def writeFile(link):
    #getting the timestamp to define filename
    timestamp = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y").replace(":","_")
    path =  link+"/"+ timestamp +"_Folder"
    os.makedirs(path)
    
    #writing to text file with nested clustered_data variable
    for i in range(len(clustered_data)):
        completeName = os.path.join(path, timestamp + "_text"+str(i+1)+".txt")         
        f = open(completeName,"w",encoding='utf8')
        for sentences in clustered_data[i]:
            f.write(sentences+"\n")
        f.close() 
    return path

#Functtion to take mean of vectors of all words in a sentence 
#and generate a sentence vector
def numpymean(vect):  
    if len(vect) == 0:
        return [0]*300
    else:
        nparray = []
        for i in vect.T:
            nparray.append(np.mean(i))                   
        return nparray

#Function to cluster which take k and numpy list as argument
#Returns list of clustered sentences
def clustering(numpy_arr,k):
    kmeans = KMeans(n_clusters = k, random_state = 0).fit(numpy_arr)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    #print(centroids)
    print(labels)
    for j in range(k):
        temp = []
        for i in range(len(labels)):
            if(labels[i]==j):
                temp.append(cleaning.data[i])
        clustered_data.append(temp)
    return
