import math

def sin(x,n):
    sine = 0
    for i in range(n):
        s = (-1)**i
        pi = 22/7
        y=x*(pi/180)
#sine expansion formula to find the value of every term        
        sine = sine+((y**(2.0*i+1))/math.factorial(2*i+1))*s
    return sine
x = int(input("Enter the value of 'x'in degrees:"))
n = int(input("Enter the number in terms'n':"))
print(round(sin(x,n),2))



























            




























                                                   
