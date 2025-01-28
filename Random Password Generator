import random
import string

def main():
    print("Welcome to the Password Generator!")
    
    # Get user requirements
    length = int(input("Enter the desired password length: "))
    include_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"
    
    # Check if at least one character type is selected
    if not (include_upper or include_lower or include_numbers or include_special):
        print("Error: You must include at least one type of character.")
        return
    
    # Generate and display 4 possible passwords
    print("\nHere are 4 possible passwords:")
    for _ in range(4):
        password = generate_password(length, include_upper, include_lower, include_numbers, include_special)
        print(password)

def generate_password(length, include_upper, include_lower, include_numbers, include_special):
    # Create a pool of characters based on user requirements
    character_pool = ""
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_lower:
        character_pool += string.ascii_lowercase
    if include_numbers:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation
    
    # Ensure the password contains at least one of each required type
    password = []
    if include_upper:
        password.append(random.choice(string.ascii_uppercase))
    if include_lower:
        password.append(random.choice(string.ascii_lowercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length with random characters from the pool
    while len(password) < length:
        password.append(random.choice(character_pool))
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return ''.join(password)

# Run the program
if __name__ == "__main__":
    main()
