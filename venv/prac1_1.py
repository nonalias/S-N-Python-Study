COFFEE_PRICE=200

def run(count,change):
    if change is False:
        print("돈이 부족합니다.")
    else:
        print("커피 " + str(count) + "잔 나왔습니다. 거스름 돈은 " + str(change) + "원 입니다.")

def isRightChange(inputmoney,count):
    if(inputmoney>=count*COFFEE_PRICE):
        return True
    else:
        return False

def getChange(inputmoney,count):
    if(isRightChange(inputmoney,count) is True):
        change = inputmoney - count * COFFEE_PRICE
        return change
    else:
        return False




inputmoney=int(input("돈을 넣을 금액을 입력해 주세요 : "))

count=int(input("몇 개 뽑으시겠습니까? : "))

run(count,getChange(inputmoney,count))
