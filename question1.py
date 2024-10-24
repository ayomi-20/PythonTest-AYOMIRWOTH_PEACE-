# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
import math
squareroot = math.sqrt
x1 = int(input("Enter horizontal piont 1: "))
x2 = int(input("Enter horizontal point 2: "))
y1 = int(input("Enter vertical piont 1: "))
y2 = int(input("Enter vertical piont 2: "))
distance = squareroot((x2 - x1)**2) + ((y2 - y1)**2)
print(f"The distance between the two coordinate points(x and y) is {distance}")








# Question 1(ii)
# Write a Python program to find maximum between three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print(f"The maximum number is {number1}")
elif number2 > number1 and number2 > number3:
    print(f"The maximum number is {number2}")
else:
    print(f"The maximum number is {number3}")



