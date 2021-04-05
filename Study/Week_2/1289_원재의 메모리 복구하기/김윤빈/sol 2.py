import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    memory = list(input())
    # ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']
    # print(memory)
    # print(memory)
    # 01010101010101010101010101010101010101010101010101
    # 맨 앞자리가 0이들어올수 있으니까 string으로 변환
    # print(memory)
    # 0으로 초기화
    temp = ['0'] * len(memory)
    # print(type(temp))
    # print(temp)
    result = 0
    for i in range(len(memory)):
        # 첫 인덱스부터 자리비교시 다르면
        if memory[i] != temp[i]:
            # 바꾸는것 count
            result += 1
            # 바꿀때 memory값이 1이라면 temp뒤의 값 전부 1로 바꿔준다
            print(type(memory[i] * (len(memory) - (i))))
            temp[i:] = memory[i] * (len(memory) - (i))
            # print(temp)

    print("#{} {}".format(tc, result))
