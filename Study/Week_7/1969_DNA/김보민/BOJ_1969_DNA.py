# DNA의 수 N과 문자열의 길이 M
# nxm행렬
import sys
sys.stdin = open("input.txt")
n,m = list(map(int, input().split()))

d = []
for i in range(n):
    d.append(input())
# d =  ['TATGATAC', 'TAAGCTAC', 'AAAGATCC', 'TGAGATAC', 'TAAGATGT']

ans = 0
ans_string=''

check = {'A':0, 'C':1, 'G':2, 'T':3}
swqp_check = {v:k for k,v in check.items()}
# swqp_check = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

for col in range(m):
    # ACGT 갯수
    cnt = [0,0,0,0]
    for row in range(n):
        cnt[check[d[row][col]]] += 1

    res = max(cnt)
    # print(res, end=' ')
    # 4 4 4 5 4 5 3 4

    ans_string += swqp_check[cnt.index(res)]
    ans += (n-res)
    # Hamming Distance


print(ans_string)
print(ans)