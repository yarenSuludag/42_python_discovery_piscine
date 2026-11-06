#!/usr/bin/env python3

number = int(input())

if number > 25 :
    print("Error")
else:
    for i in range(number,26) :
      print(f"Inside the loop, my variable is {i}")