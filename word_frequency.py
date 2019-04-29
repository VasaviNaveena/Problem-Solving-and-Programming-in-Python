file=open('word.txt','r')
f = {}
x = file.read().split()
for word in x:
    if word not in f:
        f[word] = 1
    else:
        f[word] += 1
        
frequency_list = f.items()

for k,v in frequency_list:
    print(k,v)
