import csv

file_to_load = "budget_data.csv"
file_to_output = "budgetAnalysis.txt"

# Declaring Variables
totalMonths = 0
prev_revenue = 0
monthChange = []
revenue_change_list = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]
totalProfitLosses = 0

# Read the csv
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    # loop to find totals
    for row in reader:
        totalMonths = totalMonths + 1
        totalProfitLosses = totalProfitLosses + int(row["Profit/Losses"])
        # Track the revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        monthChange = monthChange + [row["Date"]]

        # Finding the greatest increase
        if (revenue_change > greatestIncrease[1]):
            greatestIncrease[0] = row["Date"]
            greatestIncrease[1] = revenue_change
        # Finding the greatest decrease
        if (revenue_change < greatestDecrease[1]):
            greatestDecrease[0] = row["Date"]
            greatestDecrease[1] = revenue_change
# find the revenue average
revenue_avg = round((sum(revenue_change_list) / (totalMonths-1)), 2)
# making the output to print and sent to text file
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total Revenue: ${totalProfitLosses}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
    f"Greatest Decrease in Revenue: {greatestDecrease[0]} (${greatestDecrease[1]})\n")
print(output)
# Export
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)