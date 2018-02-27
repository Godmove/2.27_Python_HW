num = input("How many floating point numbers do you want to multiply together:")
num = int(num)
product = 1
for i in range(0, num):
    a = input("Enter a floating point number:")
    a = float(a)
    product = product * a
print('The product is %f' %(product))
