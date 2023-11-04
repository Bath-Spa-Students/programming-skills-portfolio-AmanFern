#use a list to store multiple dictionaries containing information about multiple pets
#use for loop to print keys and values

#making list
pet_list = []

#making first dictionary
individual_pet0 = {'Pet is owned by' : 'Aman',
                   'Pet Name' : 'Nunu',
                   'Type' : 'Cat',
                   'Pet age' : '3 and a half'}

#inserting dictionary into list
pet_list.append(individual_pet0)

#making second dictionary
individual_pet1 = {'Pet is owned by' : 'Sey',
                   'Pet Name' : 'Milo',
                   'Type' : 'Cat',
                   'Pet age' : '3'}

#inserting second dictionary into list
pet_list.append(individual_pet1)

#making third dictionary
individual_pet2 = {'pet is owned by' : 'Marga',
                   'Pet Name' : 'Bea',
                   'Type' : 'Dog',
                   'Pet age' : '5'}

#inserting third dictionary into list
pet_list.append(individual_pet2)

#for loop to print
for pets in pet_list:
    for key, data in pets.items():
        print(f"The {key} is {data} \n")
        print()