#calculator.py

import math_tools as mt

num1 = float(input("Enter the first number: "))  # Convert input to float
num2 = float(input("Enter the second number: "))  # Convert input to float

string_operation = input("Would you like to add, subtract, multiply, or divide your two numbers (choose one)? ").strip().lower()

if string_operation == "add":
    print(mt.add(num1, num2))

elif string_operation == "subtract": 
    print(mt.subtract(num1, num2))

elif string_operation == "multiply":
    print(mt.multiply(num1, num2))

elif string_operation == "divide":
    print(mt.divide(num1, num2))

else:
    print("Please choose add, subtract, multiply, or divide.")
