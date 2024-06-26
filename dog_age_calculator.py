# Create A Dog Life Stage Classifier 
def dog_age_calculator(age,name):
    if age <= 2:
        print("Looks like a puppy! your dog", name, "is only", age)
    elif 3 <= age <= 9:
        print("At age", age, "your dog", name, "is now an Adult",)
    elif age >= 10:
        print ("Your dog", name, "is a senior citizen,", "can't believe they're already", age)

dog_age_calculator(2,"Diamond")

