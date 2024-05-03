#2D Arrays & Nested Dictionaries - AbdurRehman Amir
#April 30, 2024

#This entire code will 3 dictionaries with atleast one of them being nested
#Dictionaries for characters, inventory and location for the charcter
#in my TBG/RPG who's name is Nathan Drake

#Making dictionary for the character traits
#Traits such as secret identity, super power and health
Nathan_Drake = {'secret identity': 'Tom Holland' ,
          'super power': 'Insane strength' ,
          'health': '200'}
print(f"Nathan Drake's character traits:")
for typ, explain in Nathan_Drake.items():
    print(f"Nathan Drake's {typ} is {explain}")


#Dictionary for Location and descriptions
#Three locations are the waterfall, chamber and the cave
print('\n')
location = {'waterfall': ' great body of water that extends into the sky' ,
            'chamber': 'place filled with richess beyond imagination' ,
            'cave': 'mysterious place that could lead anywhere' }
for place, description in location.items():
    print(f"{place.title()} is a {description}.")

    
#Making dictionary for Nathan Drake's inventory and descriptions
#Inverntories for survival, weapons and clothing
#All have descriptions
#Moreover, weapons have damage and clothing has protection
print('\n')
survival = {'Water': 'Ultimate hydration',
            'Torch light': 'Helps you get on track during the night' ,
            'Food': 'Keeps you energized'}

weapons = {'sword': {'description' : 'Kills anyone even with the slightest touch',
                     'damage' : 50} ,
           'pocket knife': {'description' : 'Gets bigger whenever you want it to be' ,
                            'damage' : 100}}

clothing = {'big jacket': {'description' :'Acts as both a warmer and a shield' ,
            'protection' : '75'} ,
            'tough shoes': {'description' : 'Easier to climb mountains' ,
                            'protection' : '50'} ,
            'face mask': {'description' : 'Protects from cold and viruses' ,
                          'protection': '25'}}

#Storing all dictionaries into one
inventory = {'survival' : survival ,
             'weapons' : weapons ,
             'clothing' : clothing}

print("Nathan Drake's Inventory:")
#Printing survival items and its descriptions 
for key, items in inventory['survival'].items():
    print(f'*{key}')
    print(f'  description: {items}.')
    
#Printing weapon items and its descriptions  
for key, items in inventory['weapons'].items():
    print(f"*{key.title()}")
    print(f"  description: {items['description']}.")
    print(f"  damage: {items['damage']}")
    
#Printing clothing items and its descriptions 
for key, items in inventory['clothing'].items():
    print(f"*{key.title()}")
    print(f"  description: {items['description']}.")
    print(f"  protection: {items['protection']}")
    

    


