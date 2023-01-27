# *******      TASK 10      *******
# ******* Compulsory Task 2  *******
# *******    bmi_task.py     *******
# program to calculate the Person's BMI
# -------------------- xxx ------------------------

# Asking user for the weight and height
weight = int(input("Enter your weight in Kg : "))
height = float(input("Enter your height in Metres : "))

# Calculate the BMI and display it
bmi = weight / (height**2)
print(f"Your BMI is : {bmi}")

# Using control structure to classify user weight according to the BMI

if bmi >= 30:
    print("You are Obese.You seriously need to loose your weight.")
elif bmi >= 25:
    print("You are Overweight.You need to start loosing your weight.")
elif bmi >= 18.5:
    print("Congrats! Your weight is Normal.")
else:
    print("You are underweight.You need to eat healthy.")


