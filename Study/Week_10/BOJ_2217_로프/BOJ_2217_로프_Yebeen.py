N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))
rope.sort()
rope.reverse() #내림차순 정렬
ans = []
for i in range(N):
    ans.append(rope[i] * (i+1))

print(max(ans))
