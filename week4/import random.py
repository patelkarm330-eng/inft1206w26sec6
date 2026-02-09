import random


MIN_LENGTH = 8

LETTERS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIALS = ["!", "@", "#", "$", "%"]


repeat = "yes"

while repeat == "yes":

    # ---------------- Password Length ----------------
    while True:
        try:
            password_length = int(input("Enter total password length: "))
            if password_length < MIN_LENGTH:
                print("Invalid password length. Must be at least", MIN_LENGTH)
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # ---------------- Digits ----------------
    while True:
        try:
            number_of_digits = int(input("How many digits? "))
            if number_of_digits < 0:
                print("Digits cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # ---------------- Specials ----------------
    while True:
        try:
            number_of_specials = int(input("How many special characters? "))
            if number_of_specials < 0:
                print("Special characters cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # ---------------- Letters Calculation ----------------
    number_of_letters = password_length - (
        number_of_digits + number_of_specials
    )

    while number_of_letters < 0:
        print("Total characters exceed password length.")

        while True:
            try:
                number_of_digits = int(input("Re-enter digits: "))
                number_of_specials = int(input("Re-enter specials: "))
                if number_of_digits < 0 or number_of_specials < 0:
                    print("Values must be positive.")
                    continue
                break
            except ValueError:
                print("Enter valid numbers.")

        number_of_letters = password_length - (
            number_of_digits + number_of_specials
        )

    # ---------------- Password Generation ----------------
    password_list = []

    for _ in range(number_of_letters):
        password_list.append(random.choice(LETTERS))

    for _ in range(number_of_digits):
        password_list.append(random.choice(DIGITS))

    for _ in range(number_of_specials):
        password_list.append(random.choice(SPECIALS))

    random.shuffle(password_list)

    final_password = ""

    for char in password_list:
        final_password += char

    print("\nGenerated Password:", final_password)

    # ---------------- Strength Rating ----------------
    if password_length < 6:
        print("Strength: Weak")
    elif password_length < 14:
        print("Strength: Okay")
    else:
        print("Strength: Strong")

    # ✅ OPTION to show stored list
    show_list = input("Would you like to see the stored password list? (yes/no): ").lower()

    if show_list == "yes":
        print("Stored password_list:", password_list)

    repeat = input("\nGenerate another password? (yes/no): ").lower()

print("Program ended.")
