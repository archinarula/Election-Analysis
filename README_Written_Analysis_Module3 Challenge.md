# Written Analysis of the Results for the Election Audit dataset analyis with Python-Challenge 3 (Election Audit results submission to Election commission)

## Overview of Election Audit
We are performing data analysis on the given Election Results dataset with 369712 records to help Seth and Tom submit the election audit results to the election commission.The starter code was created to identify the winning candidate, their total votes and Percentage votes. The same code was modified to also provide the new insights that Election Commission required which was the voter results for each county, total votes per county and the county with largest vote turnout. The code was executed to print the output on the command line and also save the output into a text file.

### Purpose
#### Deliverable: This analysis and code consists of 2 technical analysis outputs and a written report to deliver the results required by the Election Commission for the election audit
- Deliverable 1: The Election Results Printed to the Command Line
https://github.com/archinarula/Election-Analysis/blob/main/PyPoll_Challenge.py

- Deliverable 2: The Election Results Saved to a Text File
https://github.com/archinarula/Election-Analysis/blob/main/election_analysis.txt

- Deliverable 3: A written Analysis of the Election Audit (README.md)
https://github.com/archinarula/Election-Analysis/blob/main/README_Written_Analysis_Module3%20Challenge.md

### Method: 
- Python library of CSV and OS was used to read the CSV dataset and establsh file path
- variable intialization, Lists, dictonaries were used to hold data and extract outputs
- For loops and conditionals statements with membership and logical operators were used at several places to run iterations on rows to extract results and display unique candidate names, county names, votes and percentage per candidate/county results
- with open was used with reader method to read from the CSV and with write method to  write into the text analysis file.
- F string was used to display formatted  variable outputs (strings, integers, float) to print in command line terminal and to save in the text file output


## Election-Audit Results
- Total votes cast in this congressional election= 369,711
- County Votes breakdown of the number of votes and the percentage of total votes for each county in the precinct
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
- Denver County had the largest number of votes
- Candidate Votes breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

- Winning candidate resulys: 
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

## Election-Audit Summary
- This script is easy to read with understandable comments that can be used to locate specific code sections that maybe required to be customized in future
- The code is flexible to be used for different CSV file dataset analysis by simply replacing the source CSV with the new one in the starting path of the code (file_to_load)
- the code is good to be used to analyse results with more number of candidate election results example instead of 3 candidates like in this dataset , the same code can be used to analyse data with 100+ candidate results
- the code is good to be used to analyse multiple county voting results example instead of 3 county in this dataset, Election commission can use it for more countys within one state or for multistate election audits aswell
- The code can also customized easily by changing the mathematical operators to then use for reverse analysis i.e to Print the worst performing Candidate (least votes) and worst turnout County (least  votes county)
- This code can also be used by smaller organizations like Universities or Worker associations to analyse their voting results aswell so this code is pretty much flexible to be used to anykind of big or small voting dataset analysis





