# Define a function
def GCD(a,b):

# choose the small number
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
            
    return gcd
# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The GCD of", num1,"and", num2,"is", GCD(num1, num2))
