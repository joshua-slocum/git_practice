import random

values = []
for n in range(20):
    values.append(2**n)

for value in values:
    with open('randomlist_'+str(value)+'.txt','w',encoding='UTF8') as f:
        for i in range(value):
            f.write(str(random.random()))
            f.write('\n')
            i += 1
