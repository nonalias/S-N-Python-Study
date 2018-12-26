a=input().split()
x=int(a[0])
y=int(a[1])

if 0<x<10:
    if 0<y<10:
        print(float("{0:.9f}".format(x/y)))