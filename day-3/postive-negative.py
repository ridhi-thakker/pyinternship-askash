a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
if(a > b):
    if(a > c):
        print(a, " is greatest.")
    else:
        print(b, " is greatest.")
else:
    if(b > c):
        print(b, " is greatest.")
    else:
        print(c, " is greatest.")