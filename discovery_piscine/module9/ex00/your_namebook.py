#!/usr/bin/env python3



def array_of_names(persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}):
   
   new_array = []
   for x, y in persons.items():
      new_array.append(f'{x.capitalize()} {y.capitalize()}')  
   return new_array

print(array_of_names())




