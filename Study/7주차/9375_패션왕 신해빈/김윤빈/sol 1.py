import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    temp = {}
    for i in range(N):
        item, kinds = map(str, input().split())
        # print(item, kinds)

        if kinds in temp:
            # 딕셔너리 있으면 count값 올려주기
            temp[kinds] +=1
        # 딕셔너리 key값없으면 생성
        else:
            temp[f'{kinds}'] = 1
        # {'headgear': 2, 'eyewear': 1}
    result = 1
    for i in temp.values():
        result *= (i+1)
    print(result-1)