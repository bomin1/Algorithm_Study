import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    memory = list(map(str,input()))
    # print(memory)
    # 01010101010101010101010101010101010101010101010101
    # 맨 앞자리가 0이들어올수 있으니까 string으로 변환
    # print(memory)
    # 0으로 초기화
    temp = [str(0)] * len(memory)
    result = 0
    for i in range(len(memory)):
        # 첫 인덱스부터 자리비교시 다르면
        if memory[i] != temp[i]:
            # 바꾸는것 count
            result += 1
            # 바꿀때 memory값이 1이라면 temp뒤의 값 전부 1로 바꿔준다
            if memory[i] == '1':
                # 00000000 =1
                # 11111111
                # temp[i + 1:] = '1'
                for j in range(i+1,len(temp)):
                    temp[j] ='1'
            # memory 값이 0이라면 temp의 값 전부 0으로 바꿔준다.
            else:
                # temp[i + 1:] = 0
                for j in range(i+1,len(temp)):
                    temp[j] ='0'
    print("#{} {}".format(tc, result))
