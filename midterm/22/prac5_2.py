def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum = sum + i
    if sum == num:
        return True
    else:
        return False
            
num = int(input('임의의 숫자를 입력하세요>>'))
if is_perfect(num) == True:
    print(num, 'is perfect number')
else:
    print(num, 'is not perfect number')