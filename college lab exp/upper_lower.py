string = input("Enter a string: ")
uppercase = 0
lowercase = 0

for char in string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
