# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:28:37 2019

@author: Ritik
"""
import nltk
from nltk import word_tokenize

#defining some global variables to be accessed overall
data = []
lowered_data = []


def clean(link):
    #Opening the text file and reading all lines
    text = open(link,"r",encoding='utf8')
    
    with text as t:
        lines = t.readlines()
    
    #Extracting the required data i.e. after ":" 
    for i in lines:
        if ': ' in i:
            data.append((i.split(': '))[1]) 
            
    #Tokenizing all the words in the sentences
    cleaned_text = []
    for sentence in data:
        cleaned_text.append(word_tokenize(sentence))
    
    #Adding only alpha - numeric words
    optimized_data = []
    for i in range(len(cleaned_text)):
        optimized_sentence = []
        for word in cleaned_text[i]:
            if word.isalpha() or word.isdigit():
                optimized_sentence.append(word)
                
        optimized_data.append(optimized_sentence)
            
    #putting all the world in lower case for more optimized clustering
    for sentence in optimized_data:
        temp = []
        for word in sentence:
            temp.append(word.lower())
        lowered_data.append(temp)
    
        
    return "Success"
