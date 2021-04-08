
# import sys
# input = sys.stdin.readline 



N, M = map(int,input().split())

N_name = [input()for _ in range(N)]
M_name =[input() for _ in range(M)]
N_name=set(N_name)
M_name=set(M_name)

# for 문으로 찾으면 시간초과가 남.=
#     if N_name[i] in M_name:
#         result.append(N_name[i])
# set으로 참고하여 품.
result = list(N_name& M_name)

print(len(result))
for i in sorted(result):
    print(i)