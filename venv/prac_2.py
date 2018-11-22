a=["하나","둘","셋"]

b=["양수","한자리 수"]
result=[]
for i in range(len(a)):
    for j in range(len(b)):
        result.append([a[i],b[j]])

print(result)