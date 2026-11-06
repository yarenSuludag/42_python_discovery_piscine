#!/usr/bin/env python3
import sys 
count =0
if len(sys.argv) > 1 : 
 for i in range(1,len(sys.argv)) :
    for j in range(1,len(sys.argv[i])):
        if sys.argv[i][j] == 'z' :
          count += 1 
else :
   print("none")


for x in range(count) :
        print('z', end="")