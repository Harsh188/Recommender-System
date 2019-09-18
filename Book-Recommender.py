# Book-Recommender.py
# Author: Harshith MohanKumar
# Version: 2.0
# Description:

import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("Books.csv")
# df = df[['Book-Author','Year-Of-Publication','Genre']]
features = ['Book-Author','Genre']
print(df.head())
#df['Year-Of-Publication'] = df['Year-Of-Publication'].astype(str) 

for feature in features:
 	df[feature] = df[feature].fillna('')

# print(df['Year-Of-Publication'].head())

def combine_features(row):
	#try:
	return row['Book-Author']+" "+row['Genre']
	#except:
		#print("Error",row)

df['combined_features'] = df.apply(combine_features, axis=1)
print(df.head())

# print(df['combined_features'])

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])

print(count_matrix)

cosine_sim = cosine_similarity(count_matrix)
book_user_likes = 'The Things they Carrried'
print(cosine_sim)

index = df[df.BookTitle==book_user_likes].index[0]
print(index)
similar_books = list(enumerate(cosine_sim[index]))

print(similar_books)
sorted_similar_books = sorted(similar_books, key= lambda x:x[1], reverse=True)

print(sorted_similar_books)

i = 0
for element in sorted_similar_books:
	movie_title = df[df.index==element[0]].values[0]
	print(movie_title[0])
	i+=1
	if i==4:
		break

