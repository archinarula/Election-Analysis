# import the csv access module
import csv
# import os module to open file with unknown location path
# import os

#Assign a variable for the file path 
file_to_load = 'Resources/election_results.csv'
#file_to_write ="Analysis/election_analysis.txt"

#file_to_load = os.path.join("Resources","election_results.csv")

#TO OPEN and read the csv file
#file_variable = open(Resources/election_results.csv, r)
election_data = open (file_to_load, 'r')
# #open with a 'with' statement and assign a variable to hold the file data
# with open(file_to_load) as election_data:

# To do: perform analysis/ Read the file object with the reader function.
file_reader=csv.reader(election_data)

# Print each row in the CSV file.
#for row in file_reader:
   # print(row)

#Print the header row/ skip the header row before printing in for loop.
headers = next(file_reader)
print(headers)


# write to file
#election_data = open(file_to_write, "w")

#write data to this file and use \n to put in new line
# election_data.write ("Hello World")
# election_data.write ("this is my first writing in a file via python code")
# election_data.write ("Hello World \n country 1\n country 2\n")

# Close the file.
#election_data.close()

# # The data we need to retrieve from the csv file
# 1. Total number of casted votes
# 2. List of candidates who got the votes
# 3. percentage of votes each candidate has won
# 4. total number of votes each candidate has won 
# 5. Winner of the election based on popular votes
