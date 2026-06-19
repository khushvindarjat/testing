import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Generate Password")
    print("2. View Saved Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter website/app name: ")
        length = int(input("Enter password length: "))

        password = generate_password(length)

        print("Generated Password:", password)

        save = input("Save this password? (yes/no): ")

        if save.lower() == "yes":
            file = open("passwords.txt", "a")
            file.write(f"{website} : {password}\n")
            file.close()
            print("Password saved successfully!")

    elif choice == "2":
        try:
            file = open("passwords.txt", "r")
            data = file.read()

            if data:
                print("\n--- Saved Passwords ---")
                print(data)
            else:
                print("No passwords saved yet.")

            file.close()

        except FileNotFoundError:
            print("No saved passwords found.")

    elif choice == "3":
        print("Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice. Try again.")