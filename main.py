import random
import string


def generate_password():
    length: int = int(input("Enter the desired password length: ").strip())
    include_uppercase: str = (
        input("Include uppercase letters? (yes/no): ").strip().lower()
    )
    include_special: str = (
        input("Include special characters? (yes/no): ").strip().lower()
    )
    include_digits: str = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    lower = string.ascii_lowercase
    uppercase: str = string.ascii_uppercase if include_uppercase == "yes" else ""
    special: str = string.punctuation if include_special == "yes" else ""
    digits: str = string.digits if include_digits == "yes" else ""
    all_characters: str = lower + uppercase + special + digits

    required_characters: list = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    string_password = "".join(password)
    return string_password


if __name__ == "__main__":
    password = generate_password()
    print(password)
