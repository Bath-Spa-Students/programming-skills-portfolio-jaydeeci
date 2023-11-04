# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'pumkin',
    'owner': 'john',
    'weight': 5kg,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'chico',
    'owner': 'dennis',
    'weight': 15kg,
    'eats': 'dog food',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nAll to know about the pets" + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
