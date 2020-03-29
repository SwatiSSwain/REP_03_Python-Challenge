# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#variable declaration
months=[]  
Profits_Loss=[]
monthly_change_PL=[]

csvpath = os.path.join('Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader) 

    #create lists from csv
    for row in csvreader:
        months.append(row[0])
        Profits_Loss.append(int(row[1]))

    #calculate monthly change in profits
    for i in range(len(Profits_Loss)-1):
        monthly_change_PL.append(Profits_Loss[i+1]-Profits_Loss[i])

        
#* The total number of months included in the dataset
total_months=len(months)
        
#* The net total amount of "Profit/Losses" over the entire period
net_total_amount=sum(Profits_Loss)

#* The average of the changes in "Profit/Losses" over the entire period
avg_change=round(sum(monthly_change_PL)/len(monthly_change_PL),2)

#* The greatest increase in profits (date and amount) over the entire period
max_profit=max(monthly_change_PL)
max_profit_month_idx=monthly_change_PL.index(max(monthly_change_PL))+1
max_profit_month=months[max_profit_month_idx]

#* The greatest decrease in losses (date and amount) over the entire period
min_profit=min(monthly_change_PL)
min_profit_month_idx=monthly_change_PL.index(min(monthly_change_PL))+1
min_profit_month=months[min_profit_month_idx]

#Print Analysis to Terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(total_months))
print("Total: $"+str(net_total_amount))
print("Average Change: $"+str(avg_change))
print("Greatest Increase in Profits: "+ max_profit_month +" ($" +str(max_profit) +")")
print("Greatest Decrease in Profits: "+ min_profit_month +" ($" +str(min_profit) +")")  


# Set variable for output file
output_file = os.path.join('Output','Financial_Analysis.txt')

#  Open the output file & write data

with open(output_file, "w") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print("Total Months: "+str(total_months), file=f)
    print("Total: $"+str(net_total_amount), file=f)
    print("Average Change: $"+str(avg_change), file=f)
    print("Greatest Increase in Profits: "+ max_profit_month +" ($" +str(max_profit) +")", file=f)
    print("Greatest Decrease in Profits: "+ min_profit_month +" ($" +str(min_profit) +")", file=f) 