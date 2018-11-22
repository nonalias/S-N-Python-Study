def sum(a,b):
    return str(a+b)

def sub(a,b):
    return str(a-b)

def mul(a,b):
    return str(a*b)

def div(a,b):
    return str(a/b)



a=int(input("첫 번째 수를 입력 : "))
b=int(input("두 번째 수를 입력 : "))

print("합은 "+sum(a,b))

print("차는 "+sub(a,b))

print("곱은 "+mul(a,b))

print("나눗셈은 "+div(a,b))



