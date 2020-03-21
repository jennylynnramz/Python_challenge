#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
import os
import csv

election_csv_path = os.path.join("..","PyPoll","PyPoll_data.csv")

with open(election_csv_path,'r') as election_csv:
    csvreader = csv.reader(election_csv, delimiter=',')
    csvheader = next(csvreader) 
    #print (csvheader)    
#The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
count = 0
with open(election_csv_path,'r') as election_csv:
    csvreader = csv.reader(election_csv, delimiter=',')
    csvheader = next(csvreader) 
    for line in election_csv.readlines():
        count = count + 1
    print("Total Votes Cast: " + str(count))

#A complete list of candidates who received votes
with open(election_csv_path,'r') as election_csv:
    next(election_csv)
    candidate_dictionary = {}
    for line in election_csv.readlines():
        split_line = line.split(",")
        candidate_name = split_line[2]
        if candidate_name not in candidate_dictionary:
            candidate_dictionary[candidate_name]= 1
        else:
            candidate_dictionary[candidate_name] += 1

    for candidate_name in candidate_dictionary:
        candidate_name_break_list = candidate_name.split("\n")
        candidate_name_clean = candidate_name_break_list[0]
        print("Candidate Name: " + str(candidate_name_clean) + " Total Votes: " + str(candidate_dictionary[candidate_name]))
        

    for key in candidate_dictionary:
        key_break_list = key.split("\n")
        percent_vote = round((candidate_dictionary[key] / count * 100), 2)
        print("Percent of votes: " + key_break_list[0] + " - " + str(percent_vote) + "%")
        


    #print(candidate_dictionary)


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

#In addition, your final script should both print the analysis to the terminal and export a text file with the results

