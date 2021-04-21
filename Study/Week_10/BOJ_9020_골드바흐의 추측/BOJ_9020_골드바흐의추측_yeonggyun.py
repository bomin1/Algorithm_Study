import sys
sys.stdin = open("input.txt")

T = int(input())

# 소수인지 체크하는 함수
def check(number):
    # 제곱근을 기준으로 두수의 곱으로 약수를 나타낼 수 잇따.
    for i in range(2, int(number**0.5)+1):
        # 만약 나머지가 없는 값이 존재한다면 약수가 존재한다는 것
        if not number % i:
            # 따라서 소수가 아님
            return False
    # 검사를 통과했다면 소수임
    return True


for tc in range(1, T+1):
    n = int(input())

    # 왼쪽 오른쪽수를 각각 반으로 나눠줌
    L = int(n/2)
    R = int(n/2)

    result = []

    while True:
        # 만약 둘다 소수라면 결과에 더해준다.
        if check(L) and check(R):
            result.append((L, R, R-L))

        L -= 1
        R += 1

        #  다 검사했으면 종료
        if L < 1:
            break
    # 차이값을 기준으로 정렬한다.
    result.sort(key=lambda x: x[2])
    # 가장 차이가 적은 값이 맨 앞에 오므로 이를 출력
    print(result[0][0], result[0][1])
