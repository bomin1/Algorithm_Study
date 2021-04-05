from itertools import combinations

# import sys
#
# sys.stdin = open('input.txt')

def excepting(numbers):
    N = numbers.pop(0)
    if N == 0:
        return
    else:
        # combinaitons(list,N) : list에서 N개만큼 뽑아서 조합만들기
        com = list(combinations(numbers, 6))
        for i in com:
            print(*i)
        print()


for tc in range(3):
    numbers = list(map(int, input().split()))
    excepting(numbers)
