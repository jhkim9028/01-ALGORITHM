# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

num1, num2 = map(int, input().split())

# 10으로 나눈 나머지를 더하고 거기에 10을 곱하고 다시 나머지를 더하고 10을 곱한다. 반복
rev1 = 0
rev2 = 0
a = 0
b = 0

while True:
    if num1 < 10:
            rev1 += num1
            break
    else:
        a = num1 % 10
        num1 //= 10
        rev1 += a
        rev1 *= 10
        
while True:
    if num2 < 10:
            rev2 += num2
            break
    else:
        b = num2 % 10
        num2 //= 10
        rev2 += b
        rev2 *= 10
if rev1 > rev2:
    print(rev1)
else:
    print(rev2)
# print(rev1) if rev1 > rel2 else print(rev2)
#print(rev1 if rev1 > rev2 else rev2)
#3항연산자 적용
# =================================================
# import sys

# sys.stdin = open("1_상수.txt")

# #공백을 기준으로 입력
# a, b =input().split()

# #첫글자와 마지막글자만 바꾸면 되니까 역순으로 추출
# a = int(a[::-1]) #734  --> 437
# b = int(b[::-1]) 

# #둘 중 큰 수 출력
# #print(a) if a > b else print(b)
# print(a if a > b else b)