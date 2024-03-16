num = int(input('Enter number: '))
if num%2 == 0:
    print(num,' is even')
else: 
    print(num,' is odd')
recommended_stock = ['google','amazon','samsung','tesla']
stock = input('Enter stock: ')
if stock in recommended_stock:
    print(stock, ' is in the recommended stock list')
else:
    print(stock, ' is not in the recommended stock list')
    