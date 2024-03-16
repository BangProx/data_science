num = input('제시된 숫자의 홀짝을 알려주는 프로그램입니다. 임의의 숫자를 입력하세요: ')
num = int(num)
if num%2 == 0:
    print(str(num) + '은 짝수입니다.')
else:
    print(str(num) + '은 홀수입니다.')

rcl = ['google','amazon','samsung','Tesla']
stock = input('Please enter the stock: ')
if stock in rcl:
    print(stock+'is in the recommended stock list')
else:
    print(stock+' is not in the recommended stock list')
