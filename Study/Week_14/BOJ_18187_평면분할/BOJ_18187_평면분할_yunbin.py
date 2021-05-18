N = int(input())

idx = 1
result = 1
for i in range(1,N+1):
    result += idx
    if i%3 != 0 :
        idx += 1

print(result)