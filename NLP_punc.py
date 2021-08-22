import re
import string

import pandas as pd
import unicodedata

data = pd.read_csv('amazon_alexa.tsv',delimiter='\t')

#function to remove punctuations
"""
def punctuation_removal(messy_str):
    clean_list = [char for char in messy_str if char not in string.punctuation]
    clean_str = ''.join(clean_list)
    return clean_str
"""
#function to remove accented character
def remove_accented_chars(text):
    new_text = unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode('utf-8','ignore')
    return new_text
# data['verified_reviews'] =data['verified_reviews'].apply(punctuation_removal)

def remove_special_character(text):
    pat = r'[^a-zA-z0-9]'
    return re.sub(pat,' ',text)




data['verified_reviews'] = data.apply(lambda x: remove_accented_chars(x['verified_reviews']),axis=1)
data['verified_reviews'] = data.apply(lambda x: remove_special_character(x['verified_reviews']),axis=1)
print(data['verified_reviews'])

