N = int(input())

weight = [int(input()) for _ in range(N)]


weight.sort(reverse=True)

result = 0  
for i in range(len(weight)):

    if result < (i+1)*weight[i]:
        result = (i+1) * weight[i]
    
    

print(result)
