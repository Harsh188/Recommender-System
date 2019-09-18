# Recommender-System

This is a small recommender system project which uses machine learning to develop a system which will pick out the best output based on the users inputs. 

This project is a part of the final project for the Recommender system using Machine Learning PES IO course.

## Description: ##

This program will create a dataframe from reading the file Books.csv. Then it will choose the features to which which will be used to recommend books to a user. By combining all of these features into one column it is able to perform a count matrix on the column which will then be used to find the cosine similarity between the rows. Using the cosine similarity we find a list of similar books to which the user likes. Finally we output the most similar books.