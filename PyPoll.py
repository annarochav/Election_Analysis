#We need to get the following data:
#1.Total of counties.
#2. Total of candidates.
#3. Total of Votes.
#4. Total of votes per county.
#5. Total of votes and percentage per candidate.
#6. The list of winners bye county.


#First we need to import our dependencies, os is because we have an indirect path.

import csv
import os

# Assign a variable for the file to load and the path (Folder,file)

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.

   file_reader = csv.reader(election_data)

 # Print the header row.
   headers = next(file_reader)  
   print(headers) 
   



# Last step.
# print(election_data)











