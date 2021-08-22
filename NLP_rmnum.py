import pandas as pd
import re
def drop_num(list_text):
    list_text_new = []
    for i in list_text:
        if not re.search('\d',i):
            list_text_new.append(i)

    return ''.join(list_text_new)


data = pd.read_csv('amazon_alexa.tsv',delimiter='\t')
data['verified_reviews'] =data['verified_reviews'].apply(drop_num)
print(data['verified_reviews'])