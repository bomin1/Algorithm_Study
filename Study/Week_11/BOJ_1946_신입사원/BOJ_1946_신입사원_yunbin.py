import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr= [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[0]) # 서류 1등부터 오름차순
    # print(arr)
    count =1
    temp = arr[0][1]
    for i in range(N-1):
        if temp > arr[i+1][1]:
            count +=1
            temp = arr[i+1][1]
    print(count)