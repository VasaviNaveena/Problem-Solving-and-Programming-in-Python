from collections import OrderedDict as OD

def num2roman(n):
    
    roman = OD()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(n):
        for r in roman.keys():
            x,y = divmod(n,r)
            yield roman[r] * x
            n -= (r * x)
            if n <= 0:
                break

    return"".join([a for a in roman_num(n)])                
n = int(input("Enter any number:"))    
print("Roman Number is:", num2roman(n))
