x = []
n = int(input("Enter how many numbers:"))
for i in range(n):
    a = int(input("Enter {0} number:".format(i+1)))
    x.append(a)
print("maximum number is:", max(x))
print("minimum number is:", min(x))
print("average number is:", sum(x)/len(x))
