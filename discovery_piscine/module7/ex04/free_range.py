#!/usr/bin/env python3
import sys 

list = []

if len(sys.argv) > 2 and int(sys.argv[1]) < int(sys.argv[2]):
     for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
         list.append(i)
     print(list)     

else :
 print("none")


