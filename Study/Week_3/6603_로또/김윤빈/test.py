from itertools import combinations

while True:
    test = list(map(int, input().split()))
    if test.pop(0) == 0:
        break

    com = list(combinations(test, 6))
    for i in com:
        print(*i)
    print()