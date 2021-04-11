import sys
sys.stdin = open("input.txt")


N, M = map(int, input().split())
unknown_name = [input() for _ in range(N)]
unknown_face = [input() for _ in range(M)]

unknown = list(set(unknown_name)&set(unknown_face))

unknown.sort()

print(len(unknown))
for i in range(len(unknown)):
    print(unknown[i])
