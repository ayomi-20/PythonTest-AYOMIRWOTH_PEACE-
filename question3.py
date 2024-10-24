# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
number = int(input("Enter desired number: "))
initial_number = 0
while number > 0:
    sum = number + initial_number
    if number == 0:
        print(f"The sum of numbers entered by the user is {sum}")







# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

