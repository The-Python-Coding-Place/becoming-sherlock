"""
Introduction to the problem:
A market stall seller wants to keep track of his daily income and stock.
He asked for a program that allows him to input how much of each item he sold each day,
and the program should output the total income for the day
and which items need to be re-stocked.
An item needs to be re-stocked if there are fewer than 10 items left in stock

Here's an attempt at providing the market seller with a program to do what he needs
but it still needs a bit of work
"""

items_on_sale = {
    "Coffee": [2.2, 100],  # dict values are price and number in stock, in that order
    "Tea": [1.5, 50],
    "Chocolate": [2, 30],
    "Sandwich": [3.4, 18],
}

print("Enter quantities sold for each item:")
for item in items_on_sale.key()
    daily_income = 0
    quantity_sold = input(f"{item}: ")

     daily_income += quantity_sold * items_on_sale[item][0]

    re_order_items = []
    items_on_sale[item][1] -= quantity_sold
    if items_on_sale[item] < 10:
        re_order_items.append(item)

print(f"\nIncome today: £{daily_income:0.2f}")  # notation inside {} is for formatting number
print("\nItems that need re-stocking are:")
for item in re_order_items:
    print(item)
