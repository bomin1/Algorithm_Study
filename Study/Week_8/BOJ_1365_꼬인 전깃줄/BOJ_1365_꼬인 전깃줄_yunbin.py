'''
LIS 최장증가수열 찾기 문제 .... 
이분탐색을 통해 O(nlogn) 복잡도를 가진 lis 알고리즘 짜기 
근데 못풀겠음. 아래는 최장수열 O(n^2) 이해용 
https://shoark7.github.io/programming/algorithm/3-LIS-algorithms#5
'''
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]
print(dp)
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)
print(max(dp))

-