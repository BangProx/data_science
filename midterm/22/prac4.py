rd_num = [3,100,23,44]
for num in rd_num:
    if num%3 ==0:
        print(num)

animals = ['dog','cat','parrot']
for animal in animals:
    print(animal[0])

f_list = ['intra.h','intra.c','define.h','run.py']
for f in f_list:
    if f[-1:-3:-1] == 'h.':
        print(f)

f_list = ['intra.h','intra.c','define.h','run.py']
for f in f_list:
    if f[len(f)-2:len(f)] == '.h':
        print(f)