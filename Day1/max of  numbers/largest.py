# Take numbers from the user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

#Check n1 with n2 and n3
if (n1 > n2) and (n1 > n3):
   maximum = n1
#Check n2 with n1 and n3
elif (n2 > n1) and (n2 > n3):
   maximum = n2
else:
   maximum = n3
 
print("Maximum number is",maximum)
