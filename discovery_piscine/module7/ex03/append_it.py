#!/usr/bin/env python3
import sys 
import re

if len(sys.argv) > 1 : 
   for i in range(1,len(sys.argv)) :
    
           if len(re.findall("ism",sys.argv[i])) == 0 :
                print(sys.argv[i] + "ism")
           else :
                None   
                

else :
   print("none")