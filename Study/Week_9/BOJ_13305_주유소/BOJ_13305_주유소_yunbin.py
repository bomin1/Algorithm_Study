N = int(input())


# [2 3 1] 
load = list(map(int,input().split()))


# [5 2 4 1 ]
fee = list(map(int,input().split()))

result = 0 
for i in range(len(load)):

    if fee[i] < fee[i+1]:
        fee[i+1] = fee[i]
        
    result += load[i] *fee[i]
print(result)
        



