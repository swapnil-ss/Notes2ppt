
''' $ sudo pip install pyenchant 
   pyenchant is used for word correction as well as word suggestion of the wrong words so we can use it here
   using nltk to check the tags (i.e noun, propernoun, verbs etc ) of the words present in the sentence we have detected
'''
import wikipedia
from nltk.tag import pos_tag
import enchant
import string

def correct_words(String_name):
	tagged_sent = []
	verbs = [word for word, pos in tagged_sent if pos =='VBZ']
	# we will check for the correctness if other words apart from nouns or pronouns
	words = []
	for verb in verbs :
		d = enchant.Dict("en_US")
		if d.check(verb) == True:
			words.append(verb)


	    if d.check(verb) == False:
	    	words.append(d.suggest(verb)[0])  #appending the first suggestion from suggested array

	return words


#now we can look for the second part that is summary of corrected words and nouns

# lets take an example sentence
def summary():
	sentence = "Barack Obama is president"
#getting the tag of each word after splitting the sentence
	tagged_sent = pos_tag(sentence.split())
#assuming we will search only those words which are noun or propernouns
	propernouns = [word for word, pos in tagged_sent if pos =='NNP']
	print propernouns


	nouns = [word for word, pos in tagged_sent if pos =='NN']
	print nouns
	propernoun_summary = []
	noun_summary = []
	for propernoun in propernouns:
  		search = wikipedia.search(propernoun)
  		propernoun_summary.append(wikipedia.summary(search[0],sentences=1))
  
	for noun in nouns:
  		search = wikipedia.search(propernoun)
  		noun_summary.append(wikipedia.summary(search[0],sentences=1))
	return "".join(noun_summary)
	return "".join(propernoun_summary)


