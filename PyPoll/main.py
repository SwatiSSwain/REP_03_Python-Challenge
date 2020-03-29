# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#variable declaration
voter_ID=[] 
candidate=[]
unique_list_candidates = [] 
canditate_dict={}
total_Votes=0
vote_tally=0
vote_Percent=0.0

csvpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader) 

    #append csv data to lists for voter id and candidates
    for row in csvreader:
        voter_ID.append(row[0])
        candidate.append(row[2])

    # create unique candidate list to loop through to calculate their vote count
    for x in candidate: 
        # check if exists in unique_list or not 
        if x not in unique_list_candidates: 
            unique_list_candidates.append(x) 

    #for each candidatet tally the votes
    for i in unique_list_candidates:
        for j in candidate:
            if i==j:
                vote_tally+=1
        #append cadidate:votes to dictionary
        canditate_dict.update({i:vote_tally})
        vote_tally=0

#count total votes
total_Votes=len(voter_ID)

#find the election winner
winner = max(canditate_dict, key=canditate_dict.get)

#Print Analysis to Terminal
print("Election Results")
print("-------------------------")
#* The total number of votes cast
print("Total Votes: " +str(total_Votes))
print("-------------------------")
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
 #* The total number of votes each candidate won
for i in canditate_dict:
    print(f"{i}: {round((canditate_dict[i]/total_Votes)*100):.3f}% ({canditate_dict[i]})")
print("-------------------------")
#* The winner of the election based on popular vote.
print("Winner: "+winner)
print("-------------------------")

# Set variable for output file
output_file = os.path.join('Output','Election_Results_Analysis.txt')

#  Open the output file & write data

with open(output_file, "w") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes: " +str(total_Votes), file=f)
    print("-------------------------", file=f)   
    for i in canditate_dict:
        print(f"{i}: {round((canditate_dict[i]/total_Votes)*100):.3f}% ({canditate_dict[i]})", file=f) 
    print("-------------------------", file=f)
    print("Winner: "+winner, file=f)
    print("-------------------------", file=f)