import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    numbers, n= input().split()
    numbers = [int(val) for val in numbers]
    n = int(n)
    # sorted_numbers = sorted(numbers, reverse=True)
    # print(sorted_numbers)

    for i in range(len(numbers)-1):
        max_val = numbers[i]
        max_idx = i
        for j in range(i+1,len(numbers)):
            if numbers[j] >= max_val:
                max_val = numbers[j]
                max_idx =j
        if i != max_idx:
            numbers[i], numbers[max_idx] =  numbers[max_idx],numbers[i]
            n -=1
        if n == 0:
            break

    print('#{} {}'.format(tc, ''.join(map(str, numbers))))

#  https://github.com/YJ0522771/TIL/blob/master/Study%20Note/Algorithm%20Problems/SWEA/D3/1244%20%EC%B5%9C%EB%8C%80%20%EC%83%81%EA%B8%88%20(pass)/SWEA_1244_%EC%A0%95%EB%A0%AC%26%ED%83%90%EC%83%89.py