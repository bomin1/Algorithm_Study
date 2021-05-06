import sys
sys.stdin = open("input.txt")


n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=False)

res = 0
for i in range(n):
    res += a[i]*b[i]
print(res)
    


