# 패킹(packing)
tuple1 = 10, "열", True
print(tuple1)
# 언패킹(unpacking)
a, b, c = tuple1

print(a)
print(b)
print(c)

def get_person():
    name = "가을"
    age = 23
    addr = "강남"
    return name, age, addr


result = get_person()
name, age, addr = result  # 반환된 값을 변수에 할당

print(result)
print(name)
print(age)
# 함수 내부에서 선언된 변수는 함수 내부에서만 사용할 수 있습니다.
# 따라서 함수 외부에서 직접 이 변수에 접근하면 오류가 발생합니다.

