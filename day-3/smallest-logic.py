a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a < b and a < c:
    print(a, " is smallest.")
if b < a and b < c:
    print(b, " is smallest.")
if c < a and c < b:
    print(c, " is smallest.")