print("COMPOUND INTEREST CALCULATION\n")
print("Enter the Following Details:")
PA = float(input("Enter Principle Amount: "))
T = float(input("Enter the Time period in Years: "))
R = float(input("Enter the Rate of Interest: "))

CI = PA * (pow((1 + R / 100), T)) 

print("Compound interest is", CI) 

