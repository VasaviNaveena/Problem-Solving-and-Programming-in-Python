def sorting():
    i = open("input.txt", 'r')
    Lst = i.read().strip().split()
    Lst.sort()
    for line in  Lst:
        print(line)
        with open('output.txt', 'w') as f:
            for line in Lst:
                Lst.sort()
                f.write(line)
 
sorting()
