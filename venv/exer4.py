list_ = [i for i in range(2,11,2)]

print(list_)


a= [i for i in range(1,11)]
print(a)


b=list(range(1,11))

for i in range(len(b)):
    if (b[i] % 2 == 0):
        print(b[i])
