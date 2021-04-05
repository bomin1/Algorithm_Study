import sys
from itertools import permutations
from collections import deque

# sys.stdin = open('input.txt')
# T = int(input())
#
# for tc in range(1):

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cal_count = list(map(int, sys.stdin.readline().split()))
# print(cal_count) # [2, 1, 1, 1]
cal = ['+', '-', '*', '/']
temp = []
for i in range(4):
    j = cal_count[i]
    while j:
        temp.append(cal[i])
        j -= 1
# print(temp) ['+', '+', '-', '*', '/']

cal_list = list(permutations(temp))
# print(cal_list)
# [('+', '+', '-', '*', '/'), ('+', '+', '-', '/', '*'),('+', '+', '*', '-', '/'),....]
result = deque()
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
max_result = -123111561615616
min_result = 98989849489489498
# 순열로 만든 모든 연산자 리스트
for i in cal_list:
    # 숫자 리스트
    num = deque(numbers)
    # 연산자 리스트
    cal_i = deque(i)
    # print(cal_i)
    # 연산자를 다 뽑을때까지
    while cal_i:
        # 숫자 두개를 뽑고
        first = num.popleft()
        second = num.popleft()
        # 연산자 하나를 뽑는다.
        temp = cal_i.popleft()
        #연산자에 따라 연산 처리
        if temp == '+':
            num.insert(0, int(first) + int(second))
            # print("+",num)
        elif temp == '-':
            num.insert(0, int(first) - int(second))
            # print("-",num)
        elif temp == '*':
            num.insert(0, int(first) * int(second))
        elif temp == '/':
            if first > 0:
                num.insert(0, int(first) // int(second))
            # 음수를 양수로 나눌 때는 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
            else:
                num.insert(0, -(abs(int(first)) // int(second)))
            # print("/",num)
    # print(num)
    n = num.popleft()
    if n > max_result:
        max_result = n
        # print(i)
    if n < min_result:
        min_result = n
        # print(i)
print(max_result)
print(min_result)
