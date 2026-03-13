import re

while True:
    print("1. Validate Date (DD-MM-YYYY)")
    print("2. Find and Replace Word in Sentence")
    print("3. Validate Email ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            date = input("Enter date (DD-MM-YYYY): ")
            pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"

            if re.match(pattern, date):
                print("Valid date format")
            else:
                print("Invalid date format")

        case "2":
            sentence = input("Enter a sentence: ")
            word = input("Enter the word to find: ")
            replacement = input("Enter the replacement word: ")

            result = re.sub(word, replacement, sentence)
            print("Updated sentence:", result)

        case "3":
            email = input("Enter an email ID: ")
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            if re.match(pattern, email):
                print("Valid Email ID")
            else:
                print("Invalid Email ID")

        case "4":
            print("Program ended.")
            break

        