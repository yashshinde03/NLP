import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")
data = pd.read_csv('amazon_alexa.tsv',delimiter='\t')
# text = (""My Name is Yash. I enjoy leaving my own life and My hobbies are play cricket and badminton"")
"""
doc = nlp(text)

for token in doc:
    print(token,token.pos_)

#verb list
print("Verbs : ",[token.text for token in doc if token.pos_ == "VERB"])
# Tagging is an essential feature of text processing where we tag the words into grammatical categorization"""

doc = nlp("Apple is looking at buying U.K start-up for 1 billion dollar")
for ent in doc.ents:
    print(ent.text,ent.start_char,ent.end_char,ent.label_)

