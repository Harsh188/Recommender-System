# Recommender-System

This is a small recommender system project which uses machine learning to develop a system which will pick out the best output based on the users inputs. 

This project is a part of the final project for the Recommender system using Machine Learning PES IO course.

Started: Aug 2019
Finished: Sep 2019

## Description: ##

This program will create a dataframe from reading the file Books.csv. Then it will choose the features to which which will be used to recommend books to a user. By combining all of these features into one column it is able to perform a count matrix on the column which will then be used to find the cosine similarity between the rows. Using the cosine similarity we find a list of similar books to which the user likes. Finally we output the most similar books.

## Steps: ##

Step 1: Read from CSV file

Step 2: Select your features

Step 3: Combine all of your features into one column in your dataframe
 
Step 4: Create a count matrix from this new combined column

Step 5: Compute the Cosine Similarity based on the count matrix

Step 6: Identify the index of the object you are trying to find recommendations for

Step 7: Get a list of similar objects in descending order of similarity score [First being most similar]

Step 8: Print the top 5 most recommended objects

## What I have learned: ##

During this project I picked up a whole bunch of new skills. They are as follows:

1. Pandas library
	a. Reading a csv file and storing data into a data frame
	b. Basic manipulation of a data frame
	c. Dealing with compilation errors
	d. Dealing with data format errors
	e. Accessing elements using index and vice versa
2. Count Vectorization
3. Cosine Similarity

**Note:** I have used serveral sources from the web and youtube to build this project. A major thanks to CodeHeroku and my IO mentor.



