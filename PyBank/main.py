import os
import csv

budget_data = os.path.join("..","PyBank","budget_data.csv")

#add an if statement in case the stupid file doesn't magically exist and tell it to print that something is broken
with open (budget_data, 'r') as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
#need to fix skipping header for count
    for row in csvreader:
        count_month = len(open(budget_data).readlines(  ))
    print("Total Months: " + str(count_month))

    for  in csvreader