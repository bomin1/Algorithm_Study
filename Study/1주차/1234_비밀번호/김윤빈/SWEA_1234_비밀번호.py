import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):

    N , numbers = input().split()
    numbers= list(numbers)
    N = int(N)

    i  = 0
    # print(numbers)
    while i < N-1:
        # 숫자가 같으면
        if numbers[i] == numbers[i+1]:
            # 리스트에서 지워버리고
            del(numbers[i:i+2])
            # 리스트 갯수에서 -2
            N -= 2
            # 인덱스 한칸 뒤로
            i -= 1
        else:
            i += 1


    print("#{} {}".format(tc, ''.join(map(str,numbers))))
