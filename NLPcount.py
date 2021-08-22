import pandas as pd
import string
data = pd.read_csv('amazon_alexa.tsv',delimiter='\t')
data['char_count'] = data['verified_reviews'].apply(len)#calculating character count in review
data['word_count'] = data['verified_reviews'].apply(lambda x: len(x.split()))
data['word_density'] = data['char_count']/(data['word_count']+1)
punctuation = string.punctuation
data['punctuation_count']=data['verified_reviews'].apply(lambda x: len("".join(_ for _ in x if _ in punctuation)))
print(data[['char_count','word_count','word_density','punctuation_count']].describe())
