import random
mylist = []
for i in (range(50,100)):
    mylist.append(random.randint(0,9999))
import random
mylist2 = []
for i in (range(50,100)):
    mylist2.append(random.randint(0,9999))
print('first:',mylist, 'second:', mylist2,)
mylist3 = [] 
for i in mylist:  
    if i not in mylist2:  
        mylist3.append(i) 
print(f"[{mylist3}]")
