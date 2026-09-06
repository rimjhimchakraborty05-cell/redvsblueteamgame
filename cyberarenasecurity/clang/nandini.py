import math
import string

def estimate_crack_time(password):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation


    char_set = lower
    if any(c.isupper() for c in password):
        char_set += upper
    if any(c.isdigit() for c in password):
        char_set += digits
    if any(c in special for c in password):
        char_set += special


    num_combinations = len(char_set) ** len(password)

    guesses_per_second = 1_000_000_000
    time_to_crack_seconds = num_combinations / guesses_per_second


    if time_to_crack_seconds < 60:
        return f"{time_to_crack_seconds:.2f} seconds"
    elif time_to_crack_seconds < 3600:
        return f"{time_to_crack_seconds / 60:.2f} minutes"
    elif time_to_crack_seconds < 86400:
        return f"{time_to_crack_seconds / 3600:.2f} hours"
    else:
        return f"{time_to_crack_seconds / 86400:.2f} days"

def password_strength(password):
    length = len(password)
    if length < 6:
        return "Very Weak"
    elif length < 8:
        return "Weak"
    elif length < 12:
        return "Moderate"
    elif length < 16:
        return "Strong"
    else:
        return "Very Strong"

def character_types_used(password):
    types_used = {
        "Lowercase letters": any(c.islower() for c in password),
        "Uppercase letters": any(c.isupper() for c in password),
        "Digits": any(c.isdigit() for c in password),
        "Special characters": any(c in string.punctuation for c in password)
    }
    return {k: v for k, v in types_used.items() if v}

def check_password_strength(password):
    strength = password_strength(password)
    crack_time = estimate_crack_time(password)
    types_used = character_types_used(password)
    return strength, crack_time, types_used


if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, crack_time, types_used = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print(f"Estimated Time to Crack: {crack_time}")
    print("Character Types Used:")
    for char_type, used in types_used.items():
        print(f" - {char_type}: {'Yes' if used else 'No'}")