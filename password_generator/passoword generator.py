import random
import string

def generate_password(length=12):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    
    all_characters = lower + upper + digits + symbols

    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

   
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)

    
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the desired password length (minimum 8): "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
