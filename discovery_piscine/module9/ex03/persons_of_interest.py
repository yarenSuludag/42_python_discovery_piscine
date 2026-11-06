#!/usr/bin/env python3


def famous_births(women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}):


    
    for x, y in women_scientists.items():
        print(f"{women_scientists[x]['name']} is a great scientist born in {women_scientists[x]['date_of_birth']}")

    

print(famous_births())