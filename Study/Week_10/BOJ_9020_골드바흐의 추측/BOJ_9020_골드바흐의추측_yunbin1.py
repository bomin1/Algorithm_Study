import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

T = int(input())
for _ in range(1,T+1):

    N = int(input())
    result = [] 

    for i in range(1,N//2+1,2):

        min_num,max_num = i, N-i

        min_count = 0
        idx = 3 

        while idx <= min_num:

            if min_num %idx ==0:
                min_count +=1
            idx += 2
 
        max_count = 0
        idx = 3  

        while idx <= max_num:
            if max_num % idx ==0:
                max_count +=1
            idx += 2


        if min_count ==1 and max_count ==1:
            result= [min_num,max_num]


    print(*result)