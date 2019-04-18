x = []
for i in range(5):
    n = int(input("Enter {0} number:".format(i+1)))
    x.append(n)
print("maximum number is:", max(x))
print("minimum number is:", min(x))
print("average number is:", sum(x)/len(x))
