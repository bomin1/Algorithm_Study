import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 테스트
    memory = list(input())
    # 메모리 초기값 - 얘를 바꿔줌
    memory_init=['0']*len(memory)

    print("memory : ", memory)
    print("초기값  : ", memory_init)

    cnt = 0

    for i in range(len(memory_init)):
        if memory_init[i] != memory[i]:
            # 입력으로 들어오는거로 해당 위치부터 끝까지 쭉 바꾸기
            memory_init[i:] = memory[i]*(len(memory_init)-(i))
            cnt += 1

    print("#{} {}".format(tc, cnt))

