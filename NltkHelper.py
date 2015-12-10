# -*- coding: utf-8 -*-

from nltk import Text, word_tokenize, sent_tokenize, pos_tag, ngrams, FreqDist
#from nltk.book import *
from nltk.corpus import wordnet as wn
import os, sys
from os.path import expanduser

from nltk.tag.stanford import StanfordPOSTagger

class NltkHelper:

	def __init__(self, text):
		self.text = text

		home = expanduser("~")
		
		root = os.path.dirname(os.path.realpath(__file__))
		os.environ["STANFORD_PARSER"] = root+"/stanford-postagger/stanford-postagger.jar"
		os.environ["STANFORD_MODELS"] = root+"/stanford-postagger/models/"
		
		
		_path_to_model = root + '/stanford-postagger/models/english-bidirectional-distsim.tagger'
		_path_to_jar    = root + '/stanford-postagger/stanford-postagger.jar'
		self.stanford = StanfordPOSTagger(_path_to_model, _path_to_jar)
		

		tags = self.stanford.tag(self.word_tokenize(text.lower()))
		

		

		self.sentences = sent_tokenize(text)
		
		print self.analyze()
		nouns =  self.filterNounsInText( )
		print (self.stringifyList(nouns))
		"""
		for noun in nouns:
			print self.define(noun)
		"""
		self.bigrams = ngrams(text, 2)
		#print bigrams
		self.biDist = FreqDist( self.bigrams )

		#print self.biDist



		"""
		for noun in nouns:
			print "---", noun, "-----"
			print self.define(noun)
			print self.sentenceExamples( noun ), "\n"
		"""


	def findTags(self):
		#pattern = [("AJ", NOUN/S/FWS), (FW, FW), NOUN, NOUN]
		pass

	def bigramsList(self):
		
		pass

	def stringifyList(self, list):
		output = []
		for tag in list:
			output.append( tag )
		
		return output

	def stringifyTuples(self, tuples):
		output = []
		for tag in tuples:
			output.append( (str(tag[0]), str(tag[1])) )
		
		return output


	def word_tokenize(self, input):
		return word_tokenize(input)

	def analyze(self):
		output = []
		for sentence in self.sentences:
			taggedWords = self.stanford.tag( word_tokenize( sentence.lower() ) )
			output.append(taggedWords)

		return self.stringifyTuples(taggedWords)

	
	def filterNounsInText(self):
		output = []
		nouns = ['NN', 'NS', 'NNP', 'NNPS', 'FW']

		for sentence in self.sentences:
			taggedWords = self.stanford.tag( self.word_tokenize(sentence.lower() ) )
			for item in taggedWords:
				if item[1] in nouns:
					output.append( item[0] )

		return output




	@staticmethod
	def filterNouns(self, input):
		output = []
		nouns = ['NN', 'NS', 'NNP', 'NNPS', 'FW']
		sentences = sent_tokenize(input)
		for sentence in sentences:
			taggedWords = self.stanford.tag( self.word_tokenize(sentence.lower() ) )
			for item in taggedWords:
				if item[1] in nouns:
					output.append( item[0] )

		return self.stringifyTuples(output)

	@staticmethod
	def define( self, word ):	

		definitions = []	
		try:
			synsets = wn.synsets(word)
			for synset in synsets:
				definitions.append (synset.definition())
		except ValueError:
			print "Cannot define '{0}'".format(word)

		return definitions

	def sentenceExamples( self, noun):
		output = []
		try:
			synsets = wn.synsets(noun)
			for synset in synsets:
				examples = synset.examples()
				for example in examples:
					output.append( example )
		except ValueError, AttributeError:
			print "Cannot find any example for '{0}'".format(noun)

		return output


	def filterPersonalNouns(self, sentence):
		output = []
		pNouns = ['NNP', 'NNPS', 'FW']
		taggedWords = self.stanford.tag( word_tokenize( sentence.lower() ) )

		for item in taggedWords:
			if item[1] in nouns:
				output.append( item[0] )

		return output


title = "Reports Claim Satoshi Nakamoto Might Be 44-Year Old Australian"

content  = "New reports by Wired and Gizmodo may have identified the pseudonymous creator of bitcoin, Satoshi Nakamoto, as Australian entrepreneur Craig S Wright. "
content += "WIRED cites 'an anonymous source close to Wright' who provided a cache of emails, transcripts and other documents that point to Wright's role in the creation of bitcoin. Gizmodo cited a cache of documents sourced from someone claiming to have hacked Wright’s business email account, as well as efforts to interview individuals close to him."
content += "The news outlets further claimed that Dave Kleiman, a computer forensics expert who died in April 2013, played a significant role in the creation of bitcoin. According to Gizmodo, Kleiman 'seemed to be deeply involved with the currency and Wright’s plans' and may have a significant supply of bitcoins given his early role."
content += "It should be noted that, in WIRED’s case, the evidence was presented with caution that the information might be made up – perhaps even by Wright himself."
content += "Greenberg and Branwen write:"
content += "And despite a massive trove of evidence, we still can’t say with absolute certainty that the mystery is solved. But two possibilities outweigh all others: Either Wright invented bitcoin, or he’s a brilliant hoaxer who very badly wants us to believe he did."
content += "The idea that the Wright-Satoshi connection is nothing but a hoax has been floated by other observers, though the compelling nature of the evidence published by both Gizmodo and WIRED will no doubt fuel speculation for some time to come."
content += "But who is Wright exactly? A LinkedIn account attributed to Wright remains active at the time of writing, detailing work with a series of companies including Hotwire Pre-Emptive Intelligence Group – the firm behind an effort to create a bitcoin-based bank called Denariuz. That effort later ran into problems with the Australian Tax Office (ATO)."
content += "According to a presentation for the company published in June 2014, Denariuz aimed to become 'among the second tier banks in Australia within 5-6 years'."
content += "Gizmodo traced the connection between Wright and the ATO further, suggesting that Wright invoked his involvement in bitcoin's development during a meeting with agency officials."
content += "Further, the LinkedIn post suggests that Wright had a working relationship with representatives from various agencies within the US government."
content += "As part of work with a firm called the Global Institute for Cyber Security + Research, in a capacity as vice president and director for Asia-Pacific, Wright was responsible for fostering 'executive level relationships with the National Security Agency (NSA), Department of Homeland Security (DHS), North American Space Administration and DSD and regional government bodies'."
content += "Whether he is Satoshi or not, Wright appears to have taken efforts to reduce his online visibility by deleting his Twitter account, a move that came after the account was set to private. Gizmodo reported that the tweets were set private during its investigation."
content += "Wright did not immediately respond to a request for comment. A US phone number attributed to Wright in an email sent by him to CoinDesk in May did not connect when reached."


n1 = NltkHelper( title )


n1 = NltkHelper( content )
