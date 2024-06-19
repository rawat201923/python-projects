# Pet details
species = 'Dog'
age = 5  # Age in years

# Determine the type of pet food
if species.lower() == 'dog':
    if age < 2:
        pet_food = "Puppy food"
    elif 2 <= age <= 7:
        pet_food = "Adult dog food"
    else:
        pet_food = "Senior dog food"
elif species.lower() == 'cat':
    if age < 1:
        pet_food = "Kitten food"
    elif 1 <= age <= 7:
        pet_food = "Adult cat food"
    else:
        pet_food = "Senior cat food"
else:
    pet_food = "Unknown species"

# Output the result
# print(f"Recommended pet food for a {species.lower()} aged {age} years is: {pet_food}")
print("Recommended pet food for a ",species.lower(), "aged" ,age, "years is:" ,pet_food)