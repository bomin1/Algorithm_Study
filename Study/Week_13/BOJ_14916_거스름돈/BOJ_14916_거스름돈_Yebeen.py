n = int(input())
money = 0
if n // 5 > 0:
    money += n//5
    n %= 5
    if n % 2 == 1: #5로 나눈 나머지가 홀수이면 5로 나눈 몫을 하나 줄이고 나머지에 5를 더함
        money -= 1
        n += 5
if n // 2 > 0:
    money += n//2
    n %= 2

if n != 0:
    print(-1)
else:
    print(money)