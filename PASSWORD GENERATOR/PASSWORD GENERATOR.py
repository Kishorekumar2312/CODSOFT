import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."

    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user
try:
    user_input = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(user_input))
except ValueError:
    print("Please enter a valid number.")