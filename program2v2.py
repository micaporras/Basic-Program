# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

# Function for inputing 3 numbers
def get_numbers():
    first_num = float(input("First Number: "))
    second_num = float(input("Second Number: "))
    third_num = float(input("Third Number: "))
    return first_num, second_num, third_num


# Ask for 3 number then convert and store
first_num, second_num, third_num = get_numbers()
# Test for the lowest number
if third_num < first_num < second_num or third_num < second_num < first_num:
    print(f"The lowest number is {third_num}")
elif second_num < first_num < third_num or second_num < third_num < first_num:
    print(f"The lowest number is {second_num}")
elif first_num < second_num < third_num or first_num < third_num < second_num:
    print(f"The lowest number is {first_num}")