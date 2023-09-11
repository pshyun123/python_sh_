power_l : lambda x : x * x
in_ = [1,2,3,4,5]
out_ = list(map(lambda n:n*n, in_))
print(out_)

#out_ 리스트에는 in_ 리스트의 각 요소를 제곱한 값

# 함수로 만들어서 map이나 filter의 인자로 넣는 방법
def odd(n) :
    return  n % 2 == 1
def even(n) :
    return  n % 2 == 0

# 람다를 변수로 받아 map이나 filter의 인자로 넣는 방법
lambda_add = lambda x: x % 2 == 1
lambda_even = lambda x: x % 2 == 0

print("입력 :", end=" ")
number = list(map(int, input().split())) # 여러개의 데이터를 입력 받아서 리스트 구성
odd = list(filter(lambda_add, number))
even = list(filter(even, number))

print(f"홀수 : {odd}")
print(f"짝수 : {even}")