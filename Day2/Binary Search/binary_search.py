def binary_search(lst, start, end, key):
    if not start < end:
        return -1
 
    i = (start + end)//2
    if lst[i] < key:
        return binary_search(lst, i + 1, end, key)
    elif lst[i] > key:
        return binary_search(lst, start, i, key)
    else:
        return i
 
 
lst = input('Enter the sorted list of numbers: ')
lst = lst.split()
lst = [int(x) for x in lst]
key = int(input('Enter the number to search for: '))
 
index = binary_search(lst, 0, len(lst), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
