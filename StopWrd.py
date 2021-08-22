#stopword import library
import nltk
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize
import re
# print(stopwords.words('english'))
# stop = stopwords.words('english')
# stop_words = []
"""
from nltk.tokenize import word_tokenize
text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw)
"""
#use gensim to remove stopwords
from gensim.parsing.preprocessing import remove_stopwords

text = "Nick likes to play football, however he is not too fond of tennis."
filtered_sentences = remove_stopwords(text)

print(filtered_sentences)
