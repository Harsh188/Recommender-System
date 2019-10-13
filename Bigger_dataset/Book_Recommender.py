# Book-Recommender.py
# Author: Harshith MohanKumar
# Version: 1.0

import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read from CSV file store it as a dataset
# I seperate the dataset using ";"
# I ignore faulty lines to clean the data
# I turn the years from int to string
df = pd.read_csv("BX-Books.csv", sep=';', error_bad_lines = False, \
	dtype={'Year-Of-Publication': str},encoding="latin-1", skip_blank_lines=True)
df.fillna('')

#Step 2: Select the features which are important for comparison
features = ['Book-Author','Year-Of-Publication']

# Filter out the dataset and fill in any null values
for feature in features:
 	df[feature] = df[feature].dropna()

# Step 3: Combine all of your features into one column in your dataframe
# I cast to a string to avoid concatination problems
def combine_features(row):
	return str(row['Book-Author'])+" "+str(row['Year-Of-Publication'])

# We apply the function to combine featured to all the rows
df['combined_features'] = df.apply(combine_features, axis=1)

# Grab what the user likes (In this case its hardcoded)
book_user_likes = 'Classical Mythology'

# We find out the index value of the book which the user likes
index = df[df.BookTitle==book_user_likes].index[0]

# We identify the parent features to which we will make a count_matrix
# Parent feature is the list of features which the user likes
s = str(df['combined_features'].values[index])
selected_features = s.split(' ')

# Step 4: Create a count matrix 
# This will generate a list of 0s and 1s based on the similairty 
# of the rest of the features to the parent features
# If it matches the parent feature it is alloted a 1
# If it doesnt match it is alloted a 0
count_matrix = []
count_matrix_opt = []
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
	# to optimize the code I only select the vectors with 2 are more values in common
	if count_matrix[i].count(1)>1:
		count_matrix_opt.append(count_matrix[i])

# Step 5: Compute the Cosine Similarity based on the count matrix			
cosine_sim = cosine_similarity(count_matrix_opt)

# Step 6: Get a list of similar objects in descending order of similarity score [First being most similar]
similar_books = list(enumerate(cosine_sim[index]))

# We sort the books so that we the the most similar first
sorted_similar_books = sorted(similar_books, key= lambda x:x[1], reverse=True)

# Step 7: Print the top 3 most recommended objects
i = 0
print("\n\n\n")
for element in sorted_similar_books:
	book_title = df[df.index==element[0]].values[0]
	print(book_title[1])
	i+=1
	if i==10:
		break
print("\n\n\n")		
