# *******      TASK 9      *******
# ******* Compulsory Task  *******
# *******    courier.py     *******
# program to calculate the cost of sending a parcel
# -------------------- xxx ------------------------

item_price = int(input("Enter the price for the item : "))
delivery_distance = int(input("Enter the total distance of delivery in kms : "))

# Ask user to input delivery methods and calculate the final cost of the product accordingly
delivery_method = input("Do you want 'air' or 'freight' delivery. Type 'a' or air and 'f' for freight: ")
if delivery_method == 'a':
    print(f"The final cost of product is R{item_price+(0.36 * delivery_distance)}")
else:
    print(f"The final cost of product is R{item_price + (0.25 * delivery_distance)}")

# Asking user for type of insurance and calculating the final cost of the product accordingly

insurance_type = input("Do you want full or limited insurance? Type 'f' for full and 'l' for limited: ")
if insurance_type == 'f':
    print(f"The final cost of product is R{item_price + 50.00 }")
else:
    print(f"The final cost of product is R{item_price + 25.00}")


# Asking user if it is a gift or not and calculating the final cost of the product accordingly

is_gift = input("Is it a gift? Press 'g' for gift or 'n' for no gift: ")
if is_gift == 'g':
    print(f"The final cost of the product is R{item_price + 15.00}")
else:
    print(f"The final cost of the product is R{item_price}")

# Asking user for delivery type and calculating the final cost of the product accordingly
delivery_type = input("Do you want priority or standard delivery? Press 'p' for priority or 's' for standard: ")
if delivery_type == 'p':
    print("The final cost of the product is R",str(item_price + 100.00))
else:
    print("The final cost of the product is R", str(item_price + 20.00))





































