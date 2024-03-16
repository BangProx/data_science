num = int(input('Enter number: '))
devisor_list = []
def get_devisor(x):
    for i in range(1,x):
        if x%i == 0:
            devisor_list.append(i)

get_devisor(num)
if num == sum(devisor_list):
    print('{} is perfect number'.format(num))
else:
    print('{} is not perfect number'.format(num))