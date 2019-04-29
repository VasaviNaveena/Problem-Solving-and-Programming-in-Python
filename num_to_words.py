n=int(input("Enter any number to covert in to word:"))

def num_to_word(n):
    w = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 
          19 : 'ninteen', 20 : 'twenty', 30 : 'thirty', 40 : 'fourth',
          50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
    x = 1000
    y = x * 1000

    if (n < 20):
        return w[n]

    if (n < 100):
        if n % 10 == 0:
            return w[n]
        else:
            return w[n // 10 * 10] + ' ' + w[n % 10]

    if (n < x):
        if n % 100 == 0:
            return w[n // 100] + ' hundred'
        else:
            return w[n // 100] + ' hundred ' + num_to_word(n % 100)
    if (n < y):
        if n % x == 0:
            return num_to_word(n // x) + ' thousand'
        else:
            return num_to_word(n // x) + ' thousand, ' + num_to_word(n % x)

print(num_to_word(n))
