import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Create the pool of characters to choose from
    char_pool = ''
    
    if use_letters:
        char_pool += string.ascii_letters  # Includes both lowercase and uppercase letters
    if use_numbers:
        char_pool += string.digits  # Includes numbers 0-9
    if use_symbols:
        char_pool += string.punctuation  # Includes special symbols
    
    if not char_pool:
        raise ValueError("No character sets selected. Please select at least one character type.")

    # Generate random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length should be greater than 0.")
            return
        
        # Prompt user for character type preferences
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate the password based on user preferences
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        # Display the generated password
        print(f"\nYour generated password is: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
