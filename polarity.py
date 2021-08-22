import pandas as pd

def get_polarity(text):

    textblob = textblob(str(text.encode('utf-8')))
    pol = textblob.sentiment.polarity
    return pol


data = pd.read_csv('amazon_alexa.tsv',delimiter='\t')
data['polarity'] = data['verified_reviews'].apply(get_polarity)
print(data['polarity'])
