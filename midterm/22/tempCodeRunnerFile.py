def is_prime(num):
    if(num==1):
        return False
    elif(num==2):
        return True
    else:
        for i in range(2,num):
            if num%(i+2) == 0:
                return False
            else:
                return True
        
pon = int(input('임의의 숫자를 입력하세요>>'))
if is_prime(pon) == True: 
    print(str(pon) + '은 소수가 맞습니다')
else:
    print(str(pon) + '은 소수가 아닙니다')