# Program to calculate points earned based on the number of books purchased.

# Prompt the user for the number of books purchased.
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine the points earned.
if books_purchased >= 8:
    points = 60
elif books_purchased == 6:
    points = 30
elif books_purchased == 4:
    points = 15
elif books_purchased == 2:
    points = 5
else:
    points = 0

# Display the number of points awarded.
print(f"You have earned {points} points.")
