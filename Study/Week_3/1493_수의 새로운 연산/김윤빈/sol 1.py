import sys

sys.stdin = open('input.txt')
T = int(input())

# 1 3 6 10 15 ... 10000까지 숫자 대입할려면 n(n-1) /2보다 큰 리스트 배열을 만들자.
# 대충 150x150 했는데 인덱스 에러뜸;;
# 만약에 (150,1),(150,2) 들어올수 있다. 300방으로 크게 만들자
arr = [[0] * 301 for _ in range(300)]
value = 1
# (1,1)
# (2,1),(1,2)
# (3,1),(2,2),(1,3)
for i in range(1, 300):
    temp_i = i
    for j in range(1, i + 1):
        arr[temp_i][j] = value
        value += 1
        temp_i -= 1

print(max(arr))

# print(arr)
def indexing(numbers):
    idx_x = 0
    idx_y = 0
    count = 0
    for i in range(1, len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i][j] == p or numbers[i][j] == q:
                idx_x += i
                idx_y += j
                count += 1
                if count == 2:
                    return idx_x, idx_y

    # 다돌았는데 return이 안됬다?
    # 숫자가 같을 경우
    # 숫자가 1,1 들어올경우 count를 한번밖에 못하므로
    else:
        idx_x = idx_x + idx_x
        idx_y = idx_y + idx_y
        return idx_x, idx_y


for tc in range(1, T + 1):
    p, q = map(int, input().split())

    ans = arr[indexing(arr)[0]][indexing(arr)[1]]
    print("#{} {}".format(tc, ans))
