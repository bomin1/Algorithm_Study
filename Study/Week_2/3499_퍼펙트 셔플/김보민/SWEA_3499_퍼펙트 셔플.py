import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    cards = input().split()
    res = []

    '''
    n = 짝수일때 => 6
    0 1 2    3 4 5
    A B C ㅣ D E F
    (0 3) (1 4) (2 5) -> 3 (= n // 2)만큼 차이
    '''
    if not n % 2:
        for i in range(n // 2):
            res.append(cards[i])
            res.append(cards[i + (n // 2)])





    '''
    n이 홀수일떄 => 5 -> 6//2=3-1
    0 1 2     3 4
    A B C ㅣ  D E   =>  A D B E C
    (0 3) (1 4) (2 하고 break)
    '''
    if n % 2:
        n = n+1
        for i in range(n // 2):
            if i == (n//2)-1:
                res.append(cards[i])
                break
            else:
                res.append(cards[i])
                res.append(cards[i + (n // 2)])

    print("#{}".format(tc, ), end=" ")
    print(*res)
