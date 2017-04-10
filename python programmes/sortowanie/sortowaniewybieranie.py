import random
tab = []
for i in range(0,10):
    tab.append(random.randint(1,100))
print(tab)

for i in range(0,len(tab)):
    c=tab[0]
    for t in range(0,len(tab)-1-i):
        if c>tab[t+1]:
            c = tab[t+1]
    tab.remove(c)
    tab.append(c)
print(tab)
