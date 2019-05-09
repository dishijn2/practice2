from pprint import pprint
p1 = {}
s = ''
for i in range(3):
    s=input("enter name1")
    p1[s] = int(input("enter experience1"))
p2 = {}
for i in range(3):
    s=input("enter name2").rstrip()
    p2[s] = int(input("enter experience2"))
p1.update(p2)
minx = min([i for i in p1.values()])
maxx = max([i for i in p1.values()])
for i in p1:
    if p1[i] == minx:
        del(p1[i])
        break
        
name = input("name3")
flag=0
for i in p1:
    if i == name:
        print('Exists')
        flag = 1
        break
if flag == 0:
    print('Does not Exist')
p = dict((v,k) for k,v in p1.items())
pprint(p)
for i in p1:
    if p1[i] == maxx:
        print(i)
        break
