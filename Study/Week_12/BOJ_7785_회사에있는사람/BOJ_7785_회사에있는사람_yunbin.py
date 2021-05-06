N = int(input())

result = set()
for i in range(N):
    name, status = map(str, input().split())

    if status == 'enter':
        if name not in result:
            result.add(name)
    else:
        if name in result:
            result.remove(name)

result = list(result)
result.sort(reverse=True)
# for i in range(len(result)):
#     print(result[i])
print(*result , sep='\n')