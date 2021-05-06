import sys
sys.stdin = open("input.txt")

T = 1

for tc in range(1, T+1):
    n = int(input())
    names = []
    for i in range(n):
        name, status = input().split()
        if status == 'enter':
            names.append(name)
        else:
            names.remove(name)

    names.sort(reverse=True)

    for val in names:
        print(val)



