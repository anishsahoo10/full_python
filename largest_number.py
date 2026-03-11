a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the largest")
elif b >= c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")
