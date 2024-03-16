print('[practice 4-1]')
rd_num = [3,100,23,44]
for i in rd_num:
    print(i * 3)

print('\n[practice 4-2]')
animals = ['dog', 'cat', 'parror']
for i in animals:
    print(i[0])

print('\n[practice 4-3]')
f_list = ['intra.h', 'intra.c', 'define.h','run.py']
for i in f_list:
    lastword = len(i)-1
    if i[lastword] == 'h':
        print(i)
        
print('\n[practice 4-3]')
for i in f_list:
    splitted = i.split('.')
    if(splitted[1] == 'h'):
        print(i)
