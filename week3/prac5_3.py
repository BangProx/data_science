def is_perfect(n):
    arr = []
    if n == 1:
        return True
    else:
        for i in range(1,n):
            if n/i == 0:
                arr.append(i) 
    
    sum = 0
    for i in range(0,len(arr)):
        sum+= arr[i]
    if n == sum:
        return True
    else:
        return False

num = int(input("임의의 값을 입력하세요>>"))

if is_perfect(num) == True:
    print(str(num) + '은(는) perfect number 입니다.')
else:
    print(str(num) + '은(는) perfect number가 아닙니다.')
