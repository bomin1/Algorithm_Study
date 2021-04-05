import sys

sys.stdin = open('sample_input.txt')
T = int(input())


def dfs(idx, score, calorie):
    global result
    '''
    dfs return 하는 조건에 따라 답이 달라짐
    1.dfs()들어오자말자 칼로리 체크
    2.칼로리가 안넘으면 score 체크
    3.인덱스 초과 체크 
    모든 if 문을 통과한 후에 별일없으면 재료넣어야함
    '''
    if calorie > L:  # 만약 칼로리가 초과해버렸다면 return해서 되돌아가자
        # print('초과')
        return
    if score > result:  # 만약에 score 갱신 되면 result에 바꿔넣어주자
        # print('score,칼로리',score,calorie)
        result = score
    if idx == N:  # 만약에 모든 요리를 넣었으면 끝내야지..
        # print('idx')
        return
    T, K = cal[idx][0], cal[idx][1]  # T = 점수 K = 칼로리
    # 재료 넣었다
    score += T
    calorie += K

    dfs(idx + 1, score, calorie)  # 그다음꺼 넣어보자

    # 칼로리 초과 후에 뒤돌아간뒤에 지금 메뉴 칼로리 너무 높으니까 빼고가자
    score -= T
    calorie -= K
    # print('빼기', T, K, score, calorie)
    dfs(idx + 1, score, calorie)


for tc in range(1, T + 1):
    # 재료의 수, 제한 칼로리
    N, L = map(int, input().split())
    cal = []
    for i in range(N):
        # 맛에 대한 점수와 칼로리
        cal.append(list(map(int, input().split())))
    result = 0
    dfs(0, 0, 0)
    print("#{} {}".format(tc, result))
