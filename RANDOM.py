import random
l=[]
for i in range(6):
 d=random.randint(1,10)
 if d not in l:
     l.append(d)
print(l)
