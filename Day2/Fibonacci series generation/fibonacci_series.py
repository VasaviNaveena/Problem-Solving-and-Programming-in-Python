def fibonacci(a):
    if(a <= 1):
        return a
    else:
        return(fibonacci(a-1) + fibonacci(a-2))
a = int(input("Enter the value till which you want to generate fibonacci series: "))
print("Fibonacci sequence:")
for i in range(a):
    print(fibonacci(i))
