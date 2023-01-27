# Calculating the area of triangle

side1 = int(input("Enter the side 1"))
side2 = int(input("Enter the side 2"))
side3 = int(input("Enter the side 3"))

# calculate the semi-perimeter
s = (side1 + side2 + side3)/2

# calculate the area of the triangle
triangle_area = (s * (s-side[0]) * (s-side[1]) * (s-side[2]))**0.5

print(f"The area of triangle is : {triangle_area}")
