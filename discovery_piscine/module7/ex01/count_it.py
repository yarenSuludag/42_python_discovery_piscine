#!/usr/bin/env python3
import sys 

print("parameters: ", len(sys.argv) -1 )

if len(sys.argv) > 1 : 
 for i in range(1,len(sys.argv)) :
     print(f"{sys.argv[i]} : {len(sys.argv[i])}")
else :
   print("none")
