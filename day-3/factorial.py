n = int(input("Enter a positive integer number: "))
f = 1
if n == 0:
    print("Factorial of ", n, " is: "+str(f))
else:
    for i in range(1, n+1):
        f = f*i
print("Factorial of ", n, " is: "+str(f))