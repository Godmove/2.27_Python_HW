def abs(n):
    if(n < 0):
        return -n
    else:
        return n

list= []
for i in range(0,5):
    n = input('Enter a floating point number: ')
    n = float(n)
    list.append(abs(n))

print('The result is:', list)
