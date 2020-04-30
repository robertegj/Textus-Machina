# text analytics libraries
from textblob import TextBlob
import nltk
import transformers
import json

# Returns sentiment of text input as object
def getSentiment(getSentimenttext): 
	return TextBlob(getSentimenttext).sentiment

def getSentimentScore(getSentimenttext): 
	return TextBlob(getSentimenttext).sentiment[0]

def getEntities(getEntitiestext):
	return TextBlob(getEntitiestext).tags
	
def getNouns(getNounstext):
	return TextBlob(getNounstext).noun_phrases

def getCompound(getCompoundtext):
	compounded = {}
	compounded['Sentiment'] = str(getSentiment(getCompoundtext))
	compounded['SentimentScore'] = str(getSentimentScore(getCompoundtext))
	compounded['Entities'] = str(getEntities(getCompoundtext))
	compounded['Nouns'] = str(getNouns(getCompoundtext))
	compounded = json.dumps(compounded)
	return compounded
