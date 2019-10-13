# Book-Recommender.py
# Author: Harshith MohanKumar
# Version: 3.0

import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read from CSV file
df = pd.read_csv("Books.csv")

# Step 2: Select featues for comparision
features = ['Book-Author','Genre']

# Clean up data by removing all null values within dataframe
for feature in features:
 	df[feature] = df[feature].fillna('')

# Step 3: Combine all of your features into one column in your dataframe
# We use a function to return a row combined with the Book-Author and Genre elements
def combine_features(row):
	return row['Book-Author']+" "+row['Genre']

# We apply the function to combine featured to all the rows
df['combined_features'] = df.apply(combine_features, axis=1)

# Grab what the user likes (In this case its hardcoded)
book_user_likes = 'Of Mice and men'

# We find out the index value of the book which the user likes
index = df[df.BookTitle==book_user_likes].index[0]

# We identify the parent features to which we will make a count_matrix
# Parent feature is the list of features which the user likes
selected_features = str(df['combined_features'].values[index]).split(' ')

# Step 4: Create a count matrix 
# This will generate a list of 0s and 1s based on the similairty 
# of the rest of the features to the parent features
# If it matches the parent feature it is alloted a 1
# If it doesnt match it is alloted a 0
count_matrix = []
# Nested loop for comparision of each element
for i in range(0,len(df.index)):
	count_matrix.append(list())
	for j in range(len(selected_features)):
		if selected_features[j] in str(df['combined_features'].values[i]).split(' '):
			# append 1 if found in list
			count_matrix[i].append(1)
		else:
			# append 0 otherwise
			count_matrix[i].append(0)

# Step 5: Compute the Cosine Similarity based on the count matrix			
cosine_sim = cosine_similarity(count_matrix)

# Step 6: Get a list of similar objects in descending order of similarity score [First being most similar]
similar_books = list(enumerate(cosine_sim[index]))
# We sort the books so that we the the most similar first
sorted_similar_books = sorted(similar_books, key= lambda x:x[1], reverse=True)

# Step 7: Print the top 3 most recommended objects
print("\n\n\n")
i = 0
for element in sorted_similar_books:
	book_title = df[df.index==element[0]].values[0]
	print(book_title[0])
	i+=1
	if i==3:
		break
print("\n\n\n")
