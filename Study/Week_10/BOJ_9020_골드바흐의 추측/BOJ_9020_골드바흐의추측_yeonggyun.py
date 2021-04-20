import sys
sys.stdin = open("input.txt")

T = int(input())

# 소수인지 체크하는 함수
def check(number):
    # 어차피 절반이 넘어가면 약수가 짝을 이루므로 절반정도 까지만 검사
    for i in range(2, number//2 + 2):
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

    while True:
        # 만약 둘다 소수라면 종료
        if check(L) and check(R):
            break
        else:
            # 아니라면 차이를 벌려보자
            L -= 1
            R += 1
    # 결과값 반영
    print(L, R)




