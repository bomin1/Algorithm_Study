import sys

sys.stdin = open('input.txt')

N = int(input())

arr = [[] for _ in range(51)]
for i in range(N):
    a = input()
    arr[len(a)].append(a)


for i in range(51):
    result = set()
    if arr[i]:
        for j in arr[i]:
            result.add(j)

        result =list(result)
        result.sort()
        print(*result ,sep='\n')