num = int(input('Please enter any number: '))

def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False

isTrue = is_prime(num)
if isTrue:
    print('{} is prime number'.format(num))
else:
    print('{} is not prime number'.format(num))

