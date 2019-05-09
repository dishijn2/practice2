a=int(input())
l=input()
l3=[l]
flag=0
m=sum(list(map(int,list(l))))
for i in range(1,a):
    l1=input()
    n=sum(list(map(int,list(l1))))
    if(n==m):
        flag=1
        l3.append(l1)
if(flag):
    for j in l3:
        print(j)
else:
    print("No sum-equivalent")
