num = int(input('Enter number : '))
def is_prime(x):
    b = True
    if num == 1:
        b = False
    elif num == 2:
        b = True
    for i in range(2,x):
        if x%i==0:
            b = False
    return b
         
is_true = is_prime(num)
if is_true == True:
    print(num,' is a prime number') 
else:
    print(num,' is not a prime number')