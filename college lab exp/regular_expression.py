import re

text = "My email is test@gmail.com and I love Python. Python is powerful."

#match
print("1. MATCH")

result = re.match("My", text)

if result:
    print("Match found:", result.group())
else:
    print("No match")

print()


#search
print("2. SEARCH")

result = re.search("Python", text)

if result:
    print("Search found:", result.group())

print()


#findall
print("3. FINDALL")

result = re.findall("Python", text)

print("All matches:", result)

print()


#findall
print("4. FINDITER")

result = re.finditer("Python", text)

for i in result:
    print("Found at position:", i.start())

print()

#sub
print("5. SUBSTITUTE")

result = re.sub("Python", "Java", text)

print(result)

print()

#split
print("6. SPLIT")

text2 = "apple,banana;orange"

result = re.split("[,;]", text2)

print(result)