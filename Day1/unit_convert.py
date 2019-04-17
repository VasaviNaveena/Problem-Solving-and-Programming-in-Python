#Take input values to convert 
uc1 = input ("unit would you like to convert from: ")
uc2 = input("Which unit would you like to convert to: ")
n = float(input ("Enter your value: " ))

#Calculations
if uc1 == "feet" and uc2 == "inches":
    print("%s inches" %(n*12))
elif uc1 == "inches" and uc2 == "feet":
    print("%s feet" %(n/12))
elif uc1 == "cm" and uc2 == "inches":
    print("%s inches" %(n/2.54))    
elif uc1 == "inches" and uc2 == "cm":
    print("%s cm" %(n*2.54))    
elif uc1 == "cm" and uc2 == "feet":
    print("%s feet" %(n/30.48))    
elif uc1 == "feet" and uc2 == "cm":
    print("%s cm" %(n*30.48))    
