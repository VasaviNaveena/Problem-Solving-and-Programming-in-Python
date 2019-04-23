def sorting():
    i = open("details.txt", 'r')
    Lst = i.readlines()
    Lst.sort()
    print (Lst)
    for line in  Lst:
        print(line , end='\n')
        with open('details.txt', 'w') as f:
            for line in Lst:
                Lst.sort()
                f.write(line)
 
sorting()
