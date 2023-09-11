#방법2 사용
balance = 0
def open_account(name):
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name

# 입금
def deposit(a):
    global balance
    balance += a
    print(f"{a}이 입금. 잔액은 {balance}입니다.")
    return balance + a

# 출금
def withdraw(b):
    global balance
    if balance >= b:
        balance -= b
        print(f"{b}이 출금. 잔액은{balance}")
    else:
        print(f"출금 실패. 잔액은{balance}원")

name = open_account("짱아")
deposit(10000)
withdraw(100)
print(f"{name}의 잔액은 {balance}입니다.")