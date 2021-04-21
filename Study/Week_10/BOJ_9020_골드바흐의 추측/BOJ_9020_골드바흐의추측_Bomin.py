import sys
sys.stdin = open("input.txt")
T=int(input())

def search_prime(n):
    check_prime = [i for i in range(n + 1)]
    # print('check_prime', check_prime)
    for i in range(2,int(n**0.5)+1):
        if check_prime[i] == 0:
            continue
        else:
            for j in range(i+i, n+1,i):
                check_prime[j] = 0
    print(check_prime)
    return check_prime

def solve(prime_nums):
    half_n = n//2

    for i in range(half_n,-1,-1):
        if not prime_nums[i]:
            continue
        for j in range(i,n):
            if not prime_nums[j]:
                continue
            if prime_nums[i] + prime_nums[j] == n:
                return i,j

for tc in range(1,T+1):
    n = int(input())
    prime_nums = search_prime(n)
    print(*solve(prime_nums))




