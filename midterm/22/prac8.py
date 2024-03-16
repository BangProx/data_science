import random
randlist = []
samplelist = []
rd_num = random.random()
print(rd_num)
for r in range(10):
    randlist.append(random.random()*6)
print(randlist)

samplelist = random.shuffle(randlist)
print(randlist)
samplelist = random.sample(randlist,5)
print(samplelist)