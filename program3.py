# Program 3: Life stages
# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

# Ask for age then convert and store
age = int(input("How old are you? "))
# Test for 0-12 years old
if age > 0 and age <= 12:
    print("You are a Kid")
# Test for 13-17 years old
elif age >= 13 and age <= 17:
    print("You are a Teen")
# Test for 18 years old
elif age == 18:
    print("You are a Debut")
# Test for 19 years old and above
else:
    print("You are an Adult")