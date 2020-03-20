import os
import csv

budget_data = os.path.join("..","PyBank","budget_data.csv")

#add an if statement in case the stupid file doesn't magically exist and tell it to print that something is broken
with open(budget_data, 'r+') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
     
    #The total number of months included in the dataset
    count = 0
    for line in csvfile.readlines():
        count = count + 1
    print("Months: " + str(count))
    
    
with open(budget_data, 'r+') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # The net total amount of "Profit/Losses" over the entire period
    total = 0
    for row in csvreader:
        #print(row[1])
        total = total + int(row[1])
    print("Profit/Losses net total: " + str(total))

    #The average of the changes in "Profit/Losses" over the entire period
    profit_average = round(total / count, 2)
    print("Average Change: " + str(profit_average))

    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

with open(budget_data, 'r+') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    profit = []
    for line in csvfile:
        date = line.split(",")[0]
        profit_val = float(line.split(",")[1])
        profit.append(
            {"Date": date, 
            "Profit/Losses": profit_val})
    max_value = max([profloss["Profit/Losses"] for profloss in profit])
    print("Greatest Increase: " + str(max_value))
    min_value = min([profloss["Profit/Losses"] for profloss in profit])
    print("Greatest Decrease: " + str(min_value))

    for profloss in profit:
        if profloss["Profit/Losses"] == max_value:
            print("Date: " + str(row[0] + " Value: " + str(max_value)))
    for profloss in profit:
        if profloss["Profit/Losses"] == min_value:
            print("Date: " + str(row[0] + " Value: " + str(min_value)))
            


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

