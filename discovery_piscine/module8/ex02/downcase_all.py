#!/usr/bin/env python3
import sys 

argument1 = str()


def downcase_it(argument):
    return argument.lower()

 
if len(sys.argv) > 1 : 
  for i in range(1,len(sys.argv)):
      
        argument1 = downcase_it(sys.argv[i])
        print(argument1)

else:
      print("none")    



 