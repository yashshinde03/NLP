#for lemmatization
import nltk
import spacy

""""
nlp = spacy.load('en_core_web_sm',parse =True,tag=True,entity =True)
#function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text

get_stem("we are eating and swimming ; we have been eating and swimming ; he eats and swims ; he ates and swam")
print(get_stem)
"""