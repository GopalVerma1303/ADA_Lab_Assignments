# Taking input
string = input("Enter a string: ")

# Reversing the string using slicing
reverse_string = string[::-1]

# Checking if the string is a palindrome
if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
