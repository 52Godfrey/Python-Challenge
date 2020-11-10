import os
import csv

profit = []
change_month = []
date = []

count_months = 0
total_profitloss = 0
change_profitloss = 0
initial_profit = 0


csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv.csv')


with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        count_months = count_months + 1
        
        date.append(row[0])

        profit.append(row[1])
        total_profitloss = total_profitloss + int(row[1])

        final = int(row[1])
        profit_change = total_profitloss - initial_profit

        change_month.append(profit_change)



    sum_profitloss = (change_profitloss + profit_change)
    avg_profitloss = (sum_profitloss/count_months)

    highest_change = max(change_month)
    lowest_change = min(change_month)

    highest_month = change_month.index(highest_change)
    lowest_month = change_month.index(lowest_change)

    best_month = date[highest_month]
    worst_month = date[lowest_month]

    print("-"*64)
    print("Financial Anlysis")
    print("-"*64)
    print(f"Total Months: {count_months}")
    print(f"Total: ${total_profitloss}")
    print(f"Average Change: $", round(int(avg_profitloss)))
    print(f"Greatest Increase in Profits: {best_month} ${highest_change}")
    print(f"Greatest Decrease in Losses: {worst_month} ${lowest_change}")


with open('Analysis.txt', 'w') as text:
    text.write("-"*64)
    text.write("Financial Anlysis")
    text.write("-"*64)
    text.write(f"Total Months: {count_months}")
    text.write(f"Total: ${total_profitloss}")
    text.write(f"Average Change: $ round(int(avg_profitloss))")
    text.write(f"Greatest Increase in Profits: {best_month} ${highest_change}")
    text.write(f"Greatest Decrease in Losses: {worst_month} ${lowest_change}")
