a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
if(a < b):
    print("First integer: ", a, " is smallest.")
elif(b < a):
    print("Secong integer: ", b, " is smallest.")
else:
    print("Both are equal.")