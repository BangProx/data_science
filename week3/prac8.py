import random

arr = []
print(random.random())
for i in range(10):
    arr.append(random.random()*6)
print(arr)

list_shuffled = random.shuffle(arr)
print(arr)

selected_list = random.sample(arr, 5)
print(arr)