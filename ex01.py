num = 0
balance = 0
while 1:
    print("-"*48)
    print("1.예금 | 2.출금 | 3.잔고 | 4.종료".center(40))
    print("-"*48)
    num = input("선택 > ")
    if num=='1':
        quantity = int(input("예금액 > "))
        balance += quantity
    elif num=='2':
        quantity = int(input("출금액 > "))
        balance -= quantity
    elif num=='3':
        print("잔고액 > ",balance)
    elif num=='4':
        print("프로그램 종료")
        break