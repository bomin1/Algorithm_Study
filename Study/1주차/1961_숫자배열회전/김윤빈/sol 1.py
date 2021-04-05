import sys

sys.stdin = open('input.txt')

T = int(input())

def rotate(numbers):
    result = []
    # 뒤어서 좌표 하나씩 확인하니까 규칙성이 보였음
    """
    [
    [7,4,1], 좌표화 >  [20, 10, 00]
    [8,5,2], 좌표화 >  [21, 11, 01]
    [9,6,3], 좌표화 >  [22, 12, 02] 
    ]
    i가 뒤에 j가 앞에 있는 구조인데 j가 2부터 나오네? 
    
    """
    # i 는 그대로
    for i in range(len(numbers)):
        line = []
        # j가 2부터 나오니까 바꿔서 넣자
        for j in range(len(numbers)-1,-1,-1):
            #[j][i]형태로 맞춰서 리스트에 append!
            line.append(numbers[j][i])
        # 이중리스트이니까 result로 append!
        result.append(line)
    return result



for tc in range(1, T + 1):

    N = int(input())

    numbers = [list(map(int,input().split())) for _ in range(N)]
    # 문제 이해할겸 직접 숫자 적어서 90도로 돌려서 적어보기!
    # 90도 숫자를 또 90도 돌리니까 180도가 되네
    # 90도 한번만 잘해놓으면 180도 270도는 90도의 배수로 해결할 수 있다.
    # 90도 여러번 쓸꺼니까... 함수로 만들자

    # 90도
    a1 = rotate(numbers)
    #180도
    a2 =rotate(a1)
    # 270도
    a3 = rotate(a2)

    print("#{}".format(tc))
    for i in range(len(a1)):
        # 정답형식을 위한 string 변환후 join 함수는..안쓰고 어떻게 하는지 모르겠어서..씀
        print("".join(map(str,a1[i])), "".join(map(str,a2[i])),"".join(map(str,a3[i])))