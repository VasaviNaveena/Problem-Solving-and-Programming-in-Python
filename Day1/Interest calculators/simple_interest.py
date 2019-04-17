print("SIMPLE INTEREST CALCULATION\n")
print("Enter the Following Details:")

#Take the values for principle Amount, Time,Rate of Interest
PA = float(input("Enter Principle Amount: "))
T = float(input("Enter the Time period in Years: "))
R = float(input("Enter the Rate of Interest: "))

# Calculates simple interest  
SI = (PA * R * T) / 100

print("simple interest is", SI) 
