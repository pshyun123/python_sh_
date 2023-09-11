import random
numbers = set()
while True :
    n = random.randrange(1,46)
    numbers.add(n)
    if len(numbers) == 6 : break
print(numbers)

#이 코드는 파이썬을 사용하여 1부터 45 사이의 무작위로 선택된 서로 다른 6개의 숫자를 생성하는 프로그램입니다. 코드의 주요 기능은 다음과 같습니다:

# import random: 무작위 숫자 생성을 위해 Python의 random 모듈을 가져옵니다.
# numbers = set(): 중복되지 않는 숫자를 저장하기 위한 빈 세트(set)인 numbers를 생성합니다.
# while True:: 무한 루프를 시작합니다. 이 루프는 6개의 서로 다른 숫자를 선택할 때까지 계속 실행됩니다.
# n = random.randrange(1, 46): 1부터 45 사이의 무작위 정수를 선택하여 n에 할당합니다. 이 정수는 중복될 수 있으므로 나중에 중복을 확인해야 합니다.
# numbers.add(n): 선택한 무작위 숫자 n을 numbers 세트에 추가합니다. 세트는 중복된 값이 허용되지 않으므로 중복이 자동으로 제거됩니다.
# if len(numbers) == 6: break: numbers 세트에 6개의 숫자가 저장되면 루프를 종료합니다.
# print(numbers): 6개의 서로 다른 숫자가 포함된 numbers 세트를 출력합니다.
# 이 코드는 중복되지 않는 6개의 무작위 숫자를 생성하고 이를 세트에 저장한 후 출력합니다. 이 코드를 실행할 때마다 다른 6개의 숫자가 출력됩니다.