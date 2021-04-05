'''
첫째 줄에 옮긴 횟수 K를 출력한다.
두 번째 줄부터 수행 과정을 출력한다.
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데,
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.
'''

'''
하노이의 탑
n개의 원반이 있으면 y(n)
1. n-1개는 두번째로 옮기고 y(n-1)
2. 마지막 원반은 3번으로 옮기고 1
3. 다시  n-1개 3번으로 옮김 y(n-1)
y(n) = 2 * y(n-1) + 1
'''

def hano(n,start,end):
    if n == 1:
        print(start,end)
        return

    hano(n-1,start, 6-start-end) # n-1개를 두번째 막대로옮기는 작업이니까
    print(start,end) # 제일큰거 옮기기
    hano(n-1,6-start-end,end)

n = int(input())
print(2**n-1)
hano(n,1,3)




