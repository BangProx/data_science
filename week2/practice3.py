print('Practice 1-1\n')
num = int(input('Please enter a single number >>'))

if num/2 == 0:
    print('even')
else:
    print('odd')

print('Practice 1-2\n')
recommended_stock = ['google','amazon', 'samsung','tesla']

rs = input('Please enter a single investment stock >>')
if rs in recommended_stock:
    print(rs + ' is in the recommended stock list')
else:
    print(rs + ' is not in the recommend stock list')
