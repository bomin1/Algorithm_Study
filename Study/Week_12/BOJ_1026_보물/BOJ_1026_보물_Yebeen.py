N = int(input())
A = map(int, input().split())
B = map(int,input().split())

A=sorted(A)
B=sorted(B,reverse=True)

res = 0
for i in range(N):
    res += A[i]*B[i]
print(res)
