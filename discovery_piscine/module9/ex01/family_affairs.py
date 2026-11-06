#!/usr/bin/env python3



def find_the_redheads(dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}):
    array = []
    for x, y in dupont_family.items():
      if y== 'red' :
         array.append(x)
    return array    

print(find_the_redheads())
     

