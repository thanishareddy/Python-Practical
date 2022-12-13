"""
WAP that accepts a character and performs the following:
    a. print whether the character is a letter or numeric digit or a special character
    b. if the character is a letter, print whether the letter is uppercase or lowercase
    c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output
    is NINE)
"""

test = input("Enter the test character: ")
# a)
if test.isalpha():
    print("The test character is a letter.")
elif test.isdigit():
    print("The test character is a numeric digit.")
elif test == ' ':
    print("The test character is whitespace.")
else:
    print("The test character is a special character.")

# b)
if test.isalpha():
    print("The test character is uppercase.") if test.isupper() else print("The test character is lowercase.")

# c)
out = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
       '8': 'eight', '9': 'nine', }
if test.isdigit():
    if test in out.keys():
        print(out[test])