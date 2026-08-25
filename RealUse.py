# Control flow in real life examples
sales_performance = {
    "Jan": {
        "Kathmadu": 850000,
        "Pokhara": 900000,
        "Butwal": 650000 
    },
    "Feb": {
        "Kathmandu": 880000,
        "Pokhara": 910000,
        "Butwal": 880000
    },
    "Mar": {
        "Kathmandu": 890000,
        "Pokhara": 975000,
        "Butwal": 780000
    }
}
# store total sales for each location
total_sales = {}
# Store number of month for each location
count_months = {}

# Go via each month
for month, locations in sales_performance.items():
    # go each location
    for location, sales in locations.items():
        if location in total_sales:

            total_sales[location] += sales
            count_months[location] += 1
        else:
            total_sales[location] = sales
            count_months[location] = 1

# Calculate average monthly sales
average_sales = {
    location: total_sales[location] / count_months[location]
    for location in total_sales
}

# highest average sales
max_average_sales = max(average_sales.values())

# find the location with highest average
best_location = [
    location
    for location, average in average_sales.items()
    if average == max_average_sales
]

print(f"Total Sales: {total_sales}")
print(f"\nAverage Sales: {average_sales}")
print(f"\nBest performing location: {best_location}")
