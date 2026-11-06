#!/usr/bin/env python3
first_number = int(input("Give me the first number: "))
second_number = int(input("Give me the second number: "))
print("Thank you!")


operations = ["+", "-", "/", "*"]

for i in operations:
   
    result = eval(f"{first_number} {i} {second_number}")
    print(f"{first_number} {i} {second_number} = {result}")
