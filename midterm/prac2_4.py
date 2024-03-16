rd_num = [3,100,23,44]
animals = ['dog','cat','parror']
f_list = ['intra.h','intra.c','define.h','run.py']
for num in rd_num:
    if num%3 ==0:
        print(num)
for animal in animals:
    print(animal[0])
for file in f_list:
    if file[len(file)-2:len(file)] == '.h':
        print(file)