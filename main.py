import random
import string
import easygui
from colorama import Fore, Style, init

init()


def generate_random_password(length):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = [random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits)]

    remaining_length = length - 3
    for _ in range(remaining_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = ''.join(password)
    return password


def has_special_characters(password):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in password)


def encrypt_password(password):
    encrypted = ""
    for char in password:
        encrypted += chr(ord(char) + 1)
    return encrypted


def decrypt_password(encrypted_password):
    decrypted = ""
    for char in encrypted_password:
        decrypted += chr(ord(char) - 1)
    return decrypted


def main():
    print("Welcome to the Password Registration Program!")

    while True:
        try:
            choice = input(
                "Choose an option:\n"
                "1. Generate Random Password\n"
                "2. Input Personal Password\n"
                "Enter the number of your choice: ")
            choice = int(choice)

            if choice == 1:
                length = random.randint(8, 20)
                password = generate_random_password(length)
                encrypted_password = encrypt_password(password)
                decrypted_password = decrypt_password(encrypted_password)

                messages = [
                    f"Generated Random Password: {password}",
                    f"Encrypted Password: {encrypted_password}",
                    f"Decrypted Password: {decrypted_password}",
                    "Random Password"
                ]

                for message in messages:
                    easygui.msgbox(message)

                success_message = "Random Password Generation was generated successfully!"
                print(success_message)
                easygui.msgbox(success_message)

                return

            elif choice == 2:
                while True:
                    personal_password = input("Enter your personal password (8-20 characters): ")
                    if 8 <= len(personal_password) <= 20 and not has_special_characters(personal_password):
                        encrypted_personal_password = encrypt_password(personal_password)
                        decrypted_personal_password = decrypt_password(encrypted_personal_password)

                        messages = [
                            f"Personal Password: {personal_password}",
                            f"Encrypted Password: {encrypted_personal_password}",
                            f"Decrypted Password: {decrypted_personal_password}",
                            "Personal Password"
                        ]

                        for message in messages:
                            easygui.msgbox(message)

                        success_message = "Personal Password Registration was created successfully!"
                        print(success_message)
                        easygui.msgbox(success_message)

                        return
                    else:
                        print("***********************************************************************************")
                        print(
                            Fore.RED +
                            "Error! Please enter your password as Uppercase, Lowercase, Number only!" +
                            Style.RESET_ALL)
                        print("***********************************************************************************")
            else:
                print("Invalid choice. Please Enter '1' or '2'.")
        except ValueError:
            print("------------------------------------------------------------------------------------------------")
            print(Fore.RED + "Invalid choice! Only allow using numbers! Please, Enter '1' or '2'." + Style.RESET_ALL)
            print("------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
