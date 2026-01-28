#experiment 3 : Write a program to implement various string operations.

s= input("enter string: ")
s1= input("enter another string: ")
print("basic string operations")
print("original string: ", s)
print("length:",len(s)) 
print("concatenation:", s+s1)
print("Repetation:", s*3)
print("char at index 2:",s[2])

print("case conversion")
print("uppercase:",s.upper())
print("lowercase:",s.lower())
print("title case:",s.title())
print("capitalize:",s.capitalize())
s3="AnIsH"
print("swapcase:",s3.swapcase())

print("search and count")
print("count of 'a':",s.count('a'))
print("index of 'a':",s.find('a'))
print("rfind of 'a",s.rfind('a'))
#print("index of 'a':",s.index('a'))

print("checking string properties")
print("alphabetic:",s.isalpha())
print("is numaric:",s.isnumeric())
print("is alphanumeric:",s.isalnum())
print("is lower:",s.islower())
print("is upper:",s.isupper())
print("is space:",s.isspace())
print("is title:",s.istitle())

print("start and end")
print("starts with A:", s.startswith('A'))
print("ends with n:", s.endswith('n'))

print("modification")
print("replace a with @:",s.replace('a','@'))
print("strip:", s.strip())
print("left strip:", s.lstrip())
print("right strip:", s.rstrip())

print("splitting and joining")
words= s.split()
print("splitted words:", words)
print("joining with - :", '-'.join(words))

print("alignment functions")
print("centered:", s.center(50,'*'))
print("left justified:", s.ljust(50,'-'))
print("right justified:", s.rjust(50,'+'))

print("encoding")
print("encoded string:", s.encode())
print("string comparison ")
print("s==s1:", s==s1)
print("s<s1:", s<s1)

print("reverse string")
print(s[::-1])

print("f string")
print(f"hellow my name is : {s}") 