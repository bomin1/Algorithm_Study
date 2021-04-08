import sys
sys.stdin = open("input.txt")

n,m = list(map(int, input().split()))

a = set()
b = set()
for i in range(n):
    a.add(input())
for i in range(m):
    b.add(input())

res = sorted(list(a&b))
print(len(res))
for val in res:
    print(val)


