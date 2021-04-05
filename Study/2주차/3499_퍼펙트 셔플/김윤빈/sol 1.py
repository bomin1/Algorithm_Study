import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    name = list(input().split())
    # print(N/2)
    #
    if N %2 == 0 :
        half = N//2
    else:
        # 홀 수일때
        # 2.5 >> 3까지 포함 시키기 위해
        half = N//2 +1

    # print(half)
    # print(name)
    # print(half)
    # ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
    ##3 ALAKIR LORD-JARAXXUS ALEXSTRASZA AVIANA DR-BOOM
    # 절반 나누기
    first_name = name[0:half]
    second_name = name[half:]
    result = []
    # print(first_name)
    # print(second_name)

    for i in range(N):
        # 인덱스에 따라 result에 넣어줌
        if i % 2 ==0:
            # i = 0 ,2 ,4 ...
            # first_name에 들어있는 인덱스 = 0, 1, 2 ...
            # i//2 로 맞춰줌
            result.append(first_name[i//2])
        else:
            # i = 1, 3, 5,...
            # second_name에 들어 있는 인덱스 = 0,1,2....
            # i//2 로 맞춰줌
            result.append(second_name[i//2])
    print("#{} {}".format(tc, ' '.join(result)))
