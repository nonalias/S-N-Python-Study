a=input().split(" ")
for i in range(len(a)):
    a[i]=int(a[i])
if 0<a[0]<10:
    if 0<a[1]<10:
        print(a[0] + a[1])