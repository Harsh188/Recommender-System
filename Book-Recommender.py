# Book-Recommender.py
# Author: Harshith MohanKumar
# Version: 2.0

import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the file and store it as a dataset
df = pd.read_csv("Books.csv")
# df = df[['Book-Author','Year-Of-Publication','Genre']]

# Select the features which are important for comparison
features = ['Book-Author','Genre']
print(df.head())
#df['Year-Of-Publication'] = df['Year-Of-Publication'].astype(str) 

# Filter out the dataset and fill in any null values
for feature in features:
 	df[feature] = df[feature].fillna('')

# print(df['Year-Of-Publication'].head())

# Combine all of the features into one single column
def combine_features(row):
	#try:
	return row['Book-Author']+" "+row['Genre']
	#except:
		#print("Error",row)

df['combined_features'] = df.apply(combine_features, axis=1)
# print(df.head())

# print(df['combined_features'])

# Now use the count vectorizer and transform the dataset
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])

print(count_matrix)

# Apply the cosine similarity on the transformed dataset
cosine_sim = cosine_similarity(count_matrix)

# grab what the user likes
book_user_likes = 'The Things they Carrried'
print(cosine_sim)

# find the index of the book which the user likes and make a list 
# of all the similar books related
index = df[df.BookTitle==book_user_likes].index[0]
print(index)
similar_books = list(enumerate(cosine_sim[index]))

# print(similar_books)
# Sort the books in most relevant first and print them
sorted_similar_books = sorted(similar_books, key= lambda x:x[1], reverse=True)

print(sorted_similar_books)

i = 0
for element in sorted_similar_books:
	movie_title = df[df.index==element[0]].values[0]
	print(movie_title[0])
	i+=1
	if i==4:
		break

