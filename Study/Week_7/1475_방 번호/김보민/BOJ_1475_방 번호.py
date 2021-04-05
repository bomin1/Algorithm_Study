import sys
sys.stdin = open("input.txt")

numbers = list(map(int, str(input())))
num_cnt = [0]*10

# 각 숫자별 몇개 있는지 확인
for i in numbers:
    num_cnt[i] += 1

# 6이랑 9 빼고 가장 많이 있는 수 찾기
max_cnt = 0
for i in range(10):
    if (i!=6 and i!=9):
        max_cnt = max(num_cnt[i],max_cnt)

res = max(max_cnt, (num_cnt[6]+num_cnt[9]+1)//2)
print(res)