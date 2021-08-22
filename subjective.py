import pandas as pd
from textblob import TextBlob, Word, Blobber

def get_subjectivity(text):
    textblob = TextBlob(str(text.encode('utf-8')))
    subj = textblob.sentiment.subjectivity
    return subj

def get_polarity(text):

    textblob = TextBlob(str(text.encode('utf-8')))
    pol = textblob.sentiment.polarity
    return pol


data = pd.read_csv('amazon_alexa.tsv', delimiter='\t')
data['polarity'] = data['verified_reviews'].apply(get_polarity)
data['subjectivity']=data['verified_reviews'].apply(get_subjectivity)
data['length'] = data['verified_reviews'].apply(len)

print(data[['length','polarity','subjectivity']].describe())
