
import os.path

#get the name of the current directory
current_dir=os.getcwd()

#import operating system
#import os

#import csv file
import csv

#set path

budget_data = os.path.join('/Users/jennifervincent/M3Challenge','budget_data.csv')
# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    
    #establish variables
    profit = []
    months = []
    revenue_change =[]

    #read each row of data after header
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])

    #for loop appending the revenue change list using range function
    for v in range(1, len(profit)):
        revenue_change.append((int(profit[v]) - int(profit[v-1])))

    #calculate average revenue change and use rounding function with 2 decimals
    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)

    #determine the total number of months
    total_months = len(months)
    #print(total_months)

    #greatest increase in revenue
    greatest_increase = max(revenue_change)
    #print(greatest_increase)

    #greatest decrease in revenue
    greatest_decrease = min(revenue_change)
    #print(greatest_decrease)
    
    
    #print results
    print("Financial Analysis")
    print("_"*35)
    print("Total Months:" + str(total_months))
    print("Total:" + "$" + str(sum(profit)))
    print("Average Change:" + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")


    
