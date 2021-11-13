# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description

# Ask for grade percentage, convert and store
grade = float(input('Your grade percentage: '))
# Test for 65-74 grade percentage
if grade > 64 and grade <= 74:
    print('Your grade/mark is 5.00 and your grade description is failure')
# Test for 75 grade percentage
elif grade == 75:
    print('Your grade/mark is 3.00 and your grade description is passing')
# Test for 76-78 grade percentage
elif grade >= 76 and grade <= 78:
    print('Your grade/mark is 2.75 and your grade description is satisfactory')
# Test for 79-81 grade percentage
elif grade >= 79 and grade <= 81:
    print('Your grade/mark is 2.5 and your grade description is satisfactory')
# Test for 82-84 grade percentage
elif grade >= 82 and grade <= 84:
    print('Your grade/mark is 2.25 and your grade description is good')
# Test for 85-87 grade percentage
elif grade >= 85 and grade <= 87:
    print('Your grade/mark is 2.0 and your grade description is good')
# Test for 88-90 grade percentage
elif grade >= 88 and grade <= 90:
    print('Your grade/mark is 1.75 and your grade description is very good')
# Test for 91-93 grade percentage
elif grade >= 91 and grade <= 93:
    print('Your grade/mark is 1.5 and your grade description is very good')
# Test for 94-96 grade percentage
elif grade >= 94 and grade <= 96:
    print('Your grade/mark is 1.25 and your grade description is excellent')
# Test for 97-100 grade percentage
elif grade >= 97 and grade <= 100:
    print('Your grade/mark is 1.0 and your grade description is excellent')
else:
    print('It seems like your grade is incomplete or you are withdrawn or dropped')


print('Thank you!')