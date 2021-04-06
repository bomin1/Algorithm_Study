import sys
sys.stdin = input('input.txt')

N, M = map(int,input().split())

N_name = []
M_name =[]

for _ in range(N):
    n_name = input()
    N_name.append(n_name)
for _ in range(M):
    m_name = input()
    M_name.append(m_name)

result =[]
for i in range(N):
    if N_name[i] not in M_name:
        result.append(N_name)

print(result)