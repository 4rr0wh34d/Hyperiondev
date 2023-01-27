# *******      TASK 6       *******
# ******* Compulsory Task 2 *******
# *******    shopping.py     *******
# ------------ xxx ----------------

# Getting input from the user
product1 = input("Enter name of Product 1 :")
product2 = input("Enter name of Product 2 :")
product3 = input("Enter name of Product 3 :")

# Getting input from the user converting them to floating point and finally rounding to two decimal point
price1 = round(float(input("Enter the price for Product 1 :")),2)
price2 = round(float(input("Enter the price for Product 2 :")),2)
price3 = round(float(input("Enter the price for Product 3 :")),2)

# Total price of all three products and rounding the result to 2 decimal point
total_price = round((price1 + price2 + price3),2)

# Average price of the three products
average_price = round((total_price/3),2)

print(f"The Total of {product1},{product2} and {product3} is R{total_price} and the average price of the items is R{average_price} ")
