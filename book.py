import io
import unicodedata
import string
from sets import Set
from collections import defaultdict

class Book():
  # open and read file when initializing book object
  # create empty lists for BoWs, must reset to zero/empty when calling method
  def __init__(self, file):
    self.book = io.open(file, 'rt', encoding='utf-8', newline='\n').readlines()
    self.BoWwP, self.BoWnSW, self.BoS = [], [], []
    self.wordCount = []
    self.periodCount, self.questionCount, self.exclamationCount = 0, 0, 0
    
    
      #make BoW with punctuation
    for line in self.book:    
      lineStripped= line.rstrip() 
      # Research: https://stackoverflow.com/questions/8152820/how-to-do-string-formatting-with-unicode-emdash
      linedStrippedDashRemoved = lineStripped.replace(u"\u2014", ' ') 
      lineNormalizedLowered = unicodedata.normalize('NFKD', linedStrippedDashRemoved).encode('ascii','ignore').lower().strip().split()
      #lineNoPunc = lineNormalizedLowered.translate(None, string.punctuation).split()
      for word in lineNormalizedLowered:
        self.BoWwP.append(word)
    
    #make BoS   
    import re
    for line in self.book:    
      lineStripped= line.rstrip() 
      # Research: https://stackoverflow.com/questions/8152820/how-to-do-string-formatting-with-unicode-emdash
      linedStrippedDashRemoved = lineStripped.replace(u"\u2014", ' ') 
      lineNormalizedLowered = unicodedata.normalize('NFKD', linedStrippedDashRemoved).encode('ascii','ignore').lower().strip()
      lineNoPunc = re.split(r' .', lineNormalizedLowered)
      for word in lineNoPunc:
        self.BoS.append(word)
        
    stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'either', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except','few', 'fill', 'find', 'for', 'former', 'formerly', 'found', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'namely', 'neither', 'never', 'nevertheless', 'next', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise','our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'since', 'sincere', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'this', 'those', 'though', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves']      
  
    #make BoW with no stopwords
    for line in self.book:    
      lineStripped= line.rstrip() 
      # Research: https://stackoverflow.com/questions/8152820/how-to-do-string-formatting-with-unicode-emdash
      linedStrippedDashRemoved = lineStripped.replace(u"\u2014", ' ') 
      lineNormalizedLowered = unicodedata.normalize('NFKD', linedStrippedDashRemoved).encode('ascii','ignore').lower().strip()
      lineNoPunc = lineNormalizedLowered.translate(None, string.punctuation).split()
      for word in lineNoPunc:
        if word not in stopwords:
            self.BoWnSW.append(word)

    #punctuation analysis
    punctBoW = []
    for line in self.book:    
      lineStripped= line.rstrip() 
      # Research: https://stackoverflow.com/questions/8152820/how-to-do-string-formatting-with-unicode-emdash
      linedStrippedDashRemoved = lineStripped.replace(u"\u2014", ' ') 
      lineNormalizedLowered = unicodedata.normalize('NFKD',linedStrippedDashRemoved).encode('ascii','ignore').lower().strip().split()
      for each in lineNormalizedLowered:
        punctBoW.append(each)

    wordCounter = 0
    periodLIST, questionLIST, exclamationLIST = [], [], []

    for word in punctBoW:
      wordCounter += 1
      for char in word:
        if char == ".":
          if word[-4:] == "mr." or word[-4:] == "mrs.":
            continue
          elif word[-3:] == "...":
            continue
          elif word[-1:] == '"':
            wordCounter = 0
          else:
            self.periodCount += 1
            periodLIST.append(wordCounter)
            wordCounter = 0
        elif char == "?":
          self.questionCount += 1
          questionLIST.append(wordCounter)
          wordCounter = 0
        elif char == "!":
          self.exclamationCount += 1
          exclamationLIST.append(wordCounter)
          wordCounter = 0
        else:
          continue
  
                               
  # copy dictionary into a list and sort by descending values
  def copyDictSortDes(self, DictToCopy, length = None):
    if length is None:
      length = len(DictToCopy) 
    copy, listToReturn = [], []
    for x, y in DictToCopy.items():
       copy.append((y,x))
    copy = sorted(copy, reverse = True)
    for x in copy[0:length]:
      listToReturn.append((x[1], x[0]))
    return listToReturn 
  
  # sort single words by frequency
  def getWordCount(self, listToCount = None):
    if listToCount is None:
      if not self.BoWnSW:
        listToCount = self.BoW
      else:
        listToCount = self.BoWnSW
    self.wordCount = []
    wordCount={}
    for word in listToCount:
      if word not in wordCount:
        wordCount[word] = 1
      else:
        wordCount[word] += 1
    self.wordCount = self.copyDictSortDes(wordCount)
    
  # generate ngrams from one word to 6 words
  def getNgram(self, n): 
    nGram_list = []
    if n == 1:
      unigram = self.getWordCount(self.BoW)
      return self.wordCount
    elif n == 2:
      nGram_list = zip(self.BoW, self.BoW[1:])
    elif n == 3:
      nGram_list = zip(self.BoW, self.BoW[1:], self.BoW[2:])
    elif n == 4:
      nGram_list = zip(self.BoW, self.BoW[1:], self.BoW[2:], self.BoW[3:])
    elif n == 5:
      nGram_list = zip(self.BoW, self.BoW[1:], self.BoW[2:], self.BoW[3:], self.BoW[4:])
    elif n == 6:
      nGram_list = zip(self.BoW, self.BoW[1:], self.BoW[2:], self.BoW[3:], self.BoW[4:], self.BoW[5:])
    else:
      print "Error: Please enter an n-value from 1 - 6."
      
    nGram_dict = {}
    for nGram in nGram_list:
      if nGram in nGram_dict:
        nGram_dict[nGram] += 1
      else:
        nGram_dict[nGram] = 1
    nGram = self.copyDictSortDes(nGram_dict, 50)
    return nGram
  
  
  # returns number of positive and negative words in book and lists out those words
  def sentiment(self, pos_List, neg_List):
    posCount, negCount = 0, 0
    posWordsInBook, negWordsInBook = {}, {}
    
    listToIterate = []
    if not self.BoWnSW:
        listToIterate = self.BoW
    else:
        listToIterate = self.BoWnSW

    for word in listToIterate:
      if word in pos_List:
        posCount += 1
        if word not in posWordsInBook:
          posWordsInBook[word] = 1
        else:
          posWordsInBook[word] += 1
      elif word in neg_List:
        negCount += 1
        if word not in negWordsInBook:
          negWordsInBook[word] = 1
        else:
          negWordsInBook[word] += 1
      else:
        continue

    print "Positive word count is:", posCount
    print "Negative word count is:", negCount
    print "The top 30 occuring positive words are: "
    print self.copyDictSortDes(posWordsInBook, 30)
    print "The top 30 occuring negative words are: "
    print self.copyDictSortDes(negWordsInBook, 30)
    