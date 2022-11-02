import random
range=random.randint(10,25)
list=[]
moda=[]
for s in range(range):
    list.append(round(random.random()*100))
    for j in range (len(list)):
        for l in range (len(list)):
            if j != l:
                if list[l]==list[j] and list[l] not in moda:
                    moda.append(list[j])
print("La lista es:\n",list)
print("La moda es=",moda)
