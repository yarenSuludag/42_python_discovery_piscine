#!/usr/bin/env python3
import sys 


word1 = sys.argv[1]
print('What was the parameter? ', end="")
word2 = input()

if len(sys.argv) == 2 :
     if word1 == word2 :
      print("Good job!")
     else:
      print("Nope,sorry..")

else:
    print("none")

