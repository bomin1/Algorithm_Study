from itertools import combinations

N = int(input())
N= 6
arr = [list(map(int, input().split())) for _ in range(N)]
comination_list = list(combinations(range(1, N + 1), N // 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

result =9999
for i in range(len(comination_list) // 2):
    # 앞의 팀 능력치 
    result_left = 0
    for j in list(combinations(comination_list[i], 2)):
        # combination(list,2)를 했기때문에, 팀원 두명이 나옴 
        r, c = j[0], j[1]
        # arr[r][c] + arr[c][r] 더해줘서 능력치 더해주기  
        result_left += (arr[r-1][c-1] + arr[c-1][r-1])

    # 뒤의 팀을 보기 위한 인덱스 뒤로세기 
    result_right = 0
    reverse_list = -1 - i
    for j in list(combinations(comination_list[reverse_list], 2)):
        r, c = j[0], j[1]
        result_right += (arr[r-1][c-1] + arr[c-1][r-1])
    # 두팀의 능력치가 최소일때 result에 저장 
    result = min(result,abs(result_left-result_right))
print(result)
