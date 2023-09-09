a, b, c = map(int, input("정수 입력:").split())
if a > b :
    if a > c : print(a) # a > b,c
    else : print(c) # c > a > b
else : #a < b
    if b > c: print(b)
    else : print(c) # a < b < c

