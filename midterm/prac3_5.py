import random
print(random.random())

rand_list = []
for i in range(10):
    rand_list.append(random.random()*6)
print(rand_list)

random.shuffle(rand_list)
print(rand_list)

selected_list = random.sample(rand_list,5)
print(selected_list)