#!/usr/bin/env python3
import sys 

import re

if len(sys.argv) == 3 :

    how_many = len(re.findall(sys.argv[1], sys.argv[2]))
    print(how_many)
   
else :
    print('none')
