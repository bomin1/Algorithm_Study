import sys
sys.stdin = open("input.txt")

N = int(input())
ropes = [int(input()) for _ in range(N)]

# 전반적인 원리
# 로브들이 모두 동일한 힘을 감당 할 수 있으므로 제일작은 로프부터검사
# 그다음 로프를 검사할 때는 이전에 검사했던 작은 로프는 제외시키므로 갯수 1감소

# 로프 정렬
ropes.sort()

# 나올수 있는 총 케이스 초기값
cases = []

# 로프의 개수만큼 반복하여 검사
for i in range(len(ropes)):
    # 가장 작은 로프부터 검사하며 갯수는 하나씩 감소
    cases.append(ropes[i] * (len(ropes) - i))

# 그중 제일 큰 값이 결과값
result = max(cases)

print(result)