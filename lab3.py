while True:
    a=input().split()
    N=int(a[0])
    X=int(a[1])
    if 1<=N<=10000:
        if 1<=X<=10000:
            break
list=[]
while True:
    list = input().split()
    list = [int(i) for i in list]
    if len(list)==N:
        break
for i in range(len(list)):
    if list[i]<X:
        print(list[i],end=" ")


