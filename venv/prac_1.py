COFFEE_PRICE=200

def getChange(inputmoney,count):
    change=inputmoney-count*COFFEE_PRICE
    return change

inputmoney=int(input("돈을 넣을 금액을 입력해 주세요 : "))

count=int(input("몇 개 뽑으시겠습니까? : "))

print("커피 "+str(count)+"잔 나왔습니다. 거스름 돈은 "+str(getChange(inputmoney,count))+"원 입니다.")