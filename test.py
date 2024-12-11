# Write a Python program to validate if a string is a valid palindrome, ignoring spaces and punctuation.

# Taking input from the user
inp_str = input("Enter a String : ") 
reversed_str = inp_str[::-1]  # Reversing the string and storing it into a variable

# Validation of Palindrome
if reversed_str == inp_str :  
    print("THE GIVEN STRING IS PALINDROME")
else :
    print("THE GIVEN STRING IS NOT PALINDROME")