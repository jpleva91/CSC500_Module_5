# Program to calculate the average rainfall over a specified number of years.

# Prompt the user for the number of years.
years = int(input("Enter the number of years: "))

# Initialize the total rainfall accumulator.
total_rainfall = 0.0

# Loop through each year and month to accumulate rainfall data.
for year in range(1, years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for year {year}, month {month}: "))
        total_rainfall += rainfall

# Calculate the total number of months.
total_months = years * 12

# Calculate the average rainfall.
average_rainfall = total_rainfall / total_months

# Display the results.
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
