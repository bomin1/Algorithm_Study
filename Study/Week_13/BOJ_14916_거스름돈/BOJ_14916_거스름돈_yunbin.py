N = int(input())

change = {
    # 나머지: [5원 ,2원]
    0: [0, 0],
    1: [-1, 3], 
    2: [0, 1],
    3: [-1, 4],
    4: [0, 2],
}

five = 0
second = 0
temp = (N % 5)
five += (N // 5 + change[temp][0])
second += change[temp][1]

if N == 1 or N == 3:
    print(-1)
else:
    print(five + second)
