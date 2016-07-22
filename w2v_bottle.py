# -*- coding: utf-8 -*-

from bottle import Bottle, run, route, template, redirect, get, post, request, debug
from bottledaemon import daemon_run

import string
import sys
import requests
from gensim.models import Word2Vec
from book import Book
import sqlite3
import cPickle as pickle
#import logging

# logger = logging.getLogger('w2vApp')
# logger.setLevel(logging.INFO)

# create logging file handler
# fh = logging.FileHandler('/w2v/w2vApp.log')

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)

# add handler to logger objects
# logger.addHandler(fh) 
# logger.info("Starting bottle application.")


# turn off debugger in production
#debug(mode=True)

def w2v_results(user_submittedWord):
	"""
	Takes in a word and returns a list of 7 tuples of similar words.
	If the word has not been previously entered by a user, the w2v model is ran and the results are pickled and saved into hp_w2v db
	Otherwise, the results are served directly from hp_w2v db
	"""
	# logger.info("In W2V results function")
	word2Run = user_submittedWord
	
	#open hp_w2v db connection
	conn = sqlite3.connect('/w2v/hp_w2v.db')
	c = conn.cursor()

	#check if word2Run is already in saved_words
	c.execute("SELECT * FROM saved_words WHERE word = ? ", (word2Run,))
	id_exists = c.fetchone()
	#if word is not in saved_words:
	if id_exists is None:
		#load W2V model
		model = Word2Vec.load("/w2v/hpAll_10000features_20minwords_10context")
		#find most similar words
		similar_list = model.most_similar(word2Run)
		#change cosine similarity to 2 decimal float
		#limit to 7 words
		model_formatted = []
		for each in similar_list[:7]:
	 		model_formatted.append((each[0], float("%.2f" % each[1])))
	 	#pickle results
	 	pData = pickle.dumps(model_formatted, pickle.HIGHEST_PROTOCOL)
	 	#insert word and pickled results into saved_words table
		c.execute("INSERT OR IGNORE INTO saved_words (word, data) VALUES (?, ?)", (word2Run, sqlite3.Binary(pData) ))
		conn.commit()

	#unpickle and show results to user
	for row in c.execute("SELECT * FROM saved_words WHERE word = ? ", (word2Run,)):
		return pickle.loads(str(row[1]))

	#close connection to hp_w2v db
	conn.close()


@route('/w2v', method='POST')
def w2v():
	subWordPython = (request.forms.get('submittedWord')).lower()

	#get IP address
	ipAddress = request.environ.get('REMOTE_ADDR')

	# logger.info('word: %s ip: %s' % (subWordPython, ipAddress))

	#add subWordPython + ip address to user_words table every time.
	conn = sqlite3.connect('/w2v/hp_w2v.db')
	c = conn.cursor()
	c.execute("INSERT INTO user_words (submitted_word, ip) VALUES (?, ?)", (subWordPython, ipAddress))
	conn.commit()
	conn.close()

	#run w2v, if word is not in HP corpus, return keyerror.tpl
	try:
		wordResults = w2v_results(subWordPython)
	except KeyError as err:
		errorPage = template('/w2v/keyerror.tpl', word = subWordPython)
		return (errorPage)

	#return results to user
	output = template('/w2v/results.tpl', rows = wordResults, word = subWordPython)
	return (output)


 #call BottleDaemon script and launch a daemon in the background
if __name__ == "__main__":
  daemon_run(host='0.0.0.0', port=8080)
