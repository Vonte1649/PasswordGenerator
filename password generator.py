# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:13:48 2024

@author: Kervonte G 
"""

import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation

    # Initialize character pool with lowercase characters
    characters = lowercase_chars

    # Include uppercase characters if specified
    if use_uppercase:
        characters += uppercase_chars

    # Include digits if specified
    if use_digits:
        characters += digit_chars

    # Include special characters if specified
    if use_special_chars:
        characters += special_chars

    # Validate password length
    if length < 1:
        print("Error: Password length should be at least 1.")
        return None

    # Generate password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # User input for password criteria
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate and display the password
    generated_password = generate_password(length, include_uppercase, include_digits, include_special_chars)

    if generated_password:
        print(f"Generated Password: {generated_password}")