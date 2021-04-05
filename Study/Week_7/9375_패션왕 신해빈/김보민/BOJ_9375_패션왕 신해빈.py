import collections
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    n = int(input())

    make_dic = []
    for i in range(n):
        wear, wear_category = input().split()
        make_dic.append(wear_category)
    print(make_dic)
    # ['headgear', 'eyewear', 'headgear']
    res = collections.Counter(make_dic)
    # print(res)
    '''
    Counter({'headgear': 2, 'eyewear': 1})
    Counter({'face': 3})
    '''

    cnt = 1
    for key in res:
        cnt *= (res[key] +1)
    print(cnt-1)

    # cnt = 1
    # for i in res.values():
    #     cnt *=(i+1)
    # print(cnt-1)
