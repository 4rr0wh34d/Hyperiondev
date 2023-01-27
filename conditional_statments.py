# conditional statement examples



temperature_condition = False
weekend_status = False
sunny_status = False

# Asking user if the temperature is above 20 and changing the boolean value of temperature_condition accordingly.
temperature = input("Is the temperature greater than 20? : answer 'yes' or 'no' : ")
if temperature == "yes":
    temperature_condition = True

# Asking user if it is a weekend and setting weekend_status value to True if it is.
weekend = input("Is Today a weekend? : answer 'yes' or 'no' : ")
if weekend == "yes":
    weekend_status = True

# Asking user if it is sunny today and setting sunny_status value to False if it is
sunny = input("Is the weather sunny?  answer 'yes' or 'no' : ")
if sunny == "yes":
    sunny_status = True

# Checking the boolean value of temperature_condition,weekend_status and sunny_status and displaying
# user's outfit accordingly
if temperature_condition:
    print("You should wear a short-sleeved shirt,")
else:
    print("You should wear a long-sleeved shirt,")

if weekend_status:
    print("You should also wear a short,")
else:
    print("You should also wear a jeans,")

if sunny_status:
    print("and You should be wearing a cap.")
else:
    print("and You should be wearing a raincoat.")
