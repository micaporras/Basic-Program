# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

# Function for inputing 3 numbers
def get_numbers():
    a = float(input("First Number: "))
    b = float(input("Second Number: "))
    c = float(input("Third Number: "))
    return a, b, c


# Ask for 3 number then convert and store
a, b, c = get_numbers()
# Test for the lowest number
if c < a < b or c < b < a:
    print(f"The lowest number is {c}")
elif b < a < c or b < c < a:
    print(f"The lowest number is {b}")
elif a < b < c or a < c < b:
    print(f"The lowest number is {a}")