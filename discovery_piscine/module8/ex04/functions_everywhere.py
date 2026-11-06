#!/usr/bin/env python3
import sys  


def shrink(user_input):
    print(user_input[:8])


def enlarge(user_input):
    while len(user_input) <= 8:
        user_input = user_input + "Z"
    print(user_input)

if len(sys.argv) > 1:
   arr = sys.argv[1:]
   for i in  arr:
    if len(i) > 8:
       shrink(i)
    elif len(i) < 8:
       enlarge(i)
    elif len(i) == 8: 
       print(i)  

else:
    print("None")
  

   