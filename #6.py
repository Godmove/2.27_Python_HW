days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def cal(m, d, count):
    for i in range(0,m - 1):
        count += days_in_month[i]
    return count + d

m = input('Enter the month:')
m = int(m)
while(m < 1 or m > 12):
    m = input('Enter the month:')
    m = int(m)

d = input('Enter the day:')
d = int(d)
while(d < 1 or d > 31 or ((m == 2 and d > 28) or (m == 4 or 6 or 9 or 11) and (d > 30)) ):
    d = input('Enter the day:')
    d = int(d)
    
count = 0
cal(m, d, count)
print('%d/%d is the day number %d in the year' %(d, m, cal(m, d, count)))


