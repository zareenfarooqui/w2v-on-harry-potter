# -*- coding: utf-8 -*-
import io
import unicodedata
import string
from sets import Set
from collections import defaultdict
import sys
import requests
import json
import numpy as np
from gensim.models import word2vec
# import logging
from book import Book

hp1 = Book("/w2v/hp_books/hp1_mod.txt")
hp2 = Book("/w2v/hp_books/hp2_mod.txt")
hp3 = Book("/w2v/hp_books/hp3_mod.txt")
hp4 = Book("/w2v/hp_books/hp4_mod.txt")
hp5 = Book("/w2v/hp_books/hp5_mod.txt")
hp6 = Book("/w2v/hp_books/hp6_mod.txt")
hp7 = Book("/w2v/hp_books/hp7_mod.txt")

hpAll = hp1.BoWwP + hp2.BoWwP + hp3.BoWwP + hp4.BoWwP + hp5.BoWwP + hp6.BoWwP + hp7.BoWwP

#make bag of sentences
hpAllBoS = []
eachSentenceLIST = []

#split on sentence endings
for currWord in hpAll:
  if currWord[-1] == "." or currWord[-1] == "!" or currWord[-1] == "?" or currWord[-1] == '"' or currWord[-1] == '”':
    if currWord[-4:] == "mr." or currWord[-4:] == "mrs.":
      eachSentenceLIST.append(currWord)
    elif currWord[-3:] == "...":
      eachSentenceLIST.append(currWord)
    else:
      eachSentenceLIST.append(currWord)
      hpAllBoS.append(eachSentenceLIST[:])
      eachSentenceLIST = []
  else:
    eachSentenceLIST.append(currWord)

#remove punctuation
hpAllBoSnP = []
eachSentenceLISTnP = []
sentenceNum = 0

for sentence in hpAllBoS: 
  # Replace each word with it's transformed version
  wordNum = 0
  for word in sentence:   
    # Build a new sentence
    eachSentenceLISTnP.append(word.translate(None, string.punctuation))
    wordNum += 1
  hpAllBoSnP.append(eachSentenceLISTnP[:])
  eachSentenceLISTnP = []
  sentenceNum += 1

print "Now starting w2v"  

#start word2vec
# Set values for various parameters
num_features = 10000   # Word vector dimensionality         
min_word_count = 20    # Minimum word count                        
num_workers = 4        # Number of threads to run in parallel
context = 10           # Context window size                                                                                    
downsampling = 1e-3    # Downsample setting for frequent words

# Initialize and train the model (takes ~15 min)
print "Training model..."
model = word2vec.Word2Vec(hpAllBoSnP, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)

# If you don't plan to train the model any further, calling 
# init_sims will makes the model much more memory-efficient
model.init_sims(replace=True)

# save the model, load it later using Word2Vec.load()
model_name = "hpAll_10000features_20minwords_10context"
model.save(model_name)

print "Model saved"









    
