# 연산자 오버로딩

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y) # 한번에 값을 입력해서 이동
    def __mul__(self, other):
        return Vector2D((self.x * other.x)+ 100, (self.y * other.y) + 100)

v1 = Vector2D(1,2) # self.x와 self.y
v2 = Vector2D(3,4) # other.x와 other.y

# 그럼 v3,4,5...이렇게 늘어나면 어떻게 구분 짓지?


v3 = v1 * v2
print(v3.x, v3.y)
# 더하기 일때 4(1+3),6(2+4), 곱하기 일때__mul__ 사용됨. 103, 108
#v3.x는 (1 * 3) + 100으로 계산되어 103이 되고, v3.y는 (2 * 4) + 100으로 계산되어 108