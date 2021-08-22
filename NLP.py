import pandas as pd
data = pd.read_csv('amazon_alexa.tsv',delimiter='\t')#read dataset
# print(data.shape)#shape of dataset
# print(data.head()) Head of dataset
#If any missing value is their
# print(data.isnull().sum())
# print(data.describe()) checking description of data
# print(data.describe(include='object')) to check reviews
#To check variation for valuecount
# print(data['variation'].value_counts())
#To calculate the length of reviews
# data['length'] = data['verified_reviews'].apply(len)
# print(data['length'])
