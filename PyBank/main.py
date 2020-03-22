import os
import csv
output_file = open("PyBank_results.txt", "w")
#new file created. Changed x to w so the data here will continuously update that file
#output statements added after each print.  + "\n" needs to be added to the end so spacing in the txt isn't funky.

budget_data = os.path.join("..","PyBank","budget_data.csv")

with open(budget_data, 'r+') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")
    csvheader = next(csvreader)
   
    #The total number of months included in the dataset
    count = 0
    for line in budget_csv.readlines():
        count = count + 1
    print("Total Months: " + str(count))
    output_file.write("Total Months: " + str(count) + "\n")
#needed to be added twice in order to run the next function        
with open(budget_data, 'r+') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")
    csvheader = next(csvreader)
    # The net total amount of "Profit/Losses" over the entire period
    total = 0
    for row in csvreader:
        #print(row[1])
        total = total + int(row[1])
    print("Profit/Losses net total: " + str(total))
    output_file.write("Profit/Losses net total: " + str(total) + "\n")
    #The average of the changes in "Profit/Losses" over the entire period
    profit_average = round(total / count, 2)
    print("Average Change: " + str(profit_average))
    output_file.write("Average Change: " + str(profit_average) + "\n")
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
with open(budget_data, 'r+') as budget_csv:
    next(budget_csv)
    #creating a dictionary to hold the month and profit
    profit_dictionary = {}
    for line in budget_csv.readlines():
        split_budget_line = line.split(",")
        profit_amount = int(split_budget_line[1].split("\n")[0])
        profit_month = split_budget_line[0]
        if profit_month and profit_amount not in profit_dictionary:
            profit_dictionary[profit_month] = profit_amount
    #dictionary created. month is key, profit amount is value.
    #need to iterate to determine highest and lowest values 
    #print(profit_dictionary)
    #relevant variables
    profit_maximum = 0
    month_of_profit_maximum = ""
    for key in profit_dictionary:
        if profit_dictionary[key] > profit_maximum:
            profit_maximum = profit_dictionary[key]
            month_of_profit_maximum = key
    print("The month with the highest profit was " + str(month_of_profit_maximum) + " with a profit of $" + str(profit_maximum))
    output_file.write("The month with the highest profit was " + str(month_of_profit_maximum) + " with a profit of $" + str(profit_maximum) + "\n")

#max is solved, min is next, hopefully it works basically the same...
    #relevant variables
    profit_minimum = 0
    month_of_profit_minimum = ""
    for key in profit_dictionary:
        if profit_dictionary[key] < profit_minimum:
            profit_minimum = profit_dictionary[key]
            month_of_profit_minimum = key
    print("The month with the lowest profit was " + str(month_of_profit_minimum) + " with a loss of $" + str(profit_minimum))
    output_file.write("The month with the lowest profit was " + str(month_of_profit_minimum) + " with a loss of $" + str(profit_minimum) + "\n")

   #Day 8 of my quarantine. There are no more available grocery delivery days for at least 7 days. I don't know about furthur out because Safeway doesn't even give us the option of seeing anymore. Outlook is bleak. I may have to physically walk to trader joes to fight with the other social peasants for the last head of lettuce.
 

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#####Unused Code graveyard. For all the code that just didn't get the job done.######
##################RIP##################
# with open(budget_data, 'r+') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     csvheader = next(csvreader)
#     profit = []
#     for line in csvfile:
#         date = line.split(",")[0]
#         profit_val = float(line.split(",")[1])
#         profit.append(
#             {"Date": date, 
#             "Profit/Losses": profit_val})
#     max_value = max([profloss["Profit/Losses"] for profloss in profit])
#     print("Greatest Increase: " + str(max_value))
#     min_value = min([profloss["Profit/Losses"] for profloss in profit])
#     print("Greatest Decrease: " + str(min_value))

#     for profloss in profit:
#         if profloss["Profit/Losses"] == max_value:
#             print("Date: " + str(row[0] + " Value: " + str(max_value)))
#     for profloss in profit:
#         if profloss["Profit/Losses"] == min_value:
#             print("Date: " + str(row[0] + " Value: " + str(min_value)))

output_file.close()
