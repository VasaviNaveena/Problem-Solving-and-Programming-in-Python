#A function linear_search that takes lst and key as arguemnts
def linear_search(lst, key):
    
    for i in range(len(lst)):
        if lst[i] == key:
#Return index of key in lst if found        
            return i
#Return -1 if key not found
    return -1
 
 
lst = input('Enter the list of numbers: ')
lst = lst.split()
lst = [int(x) for x in lst]
key = int(input('Enter the number to search for: '))
 
index = linear_search(lst, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
