import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

N, Q = map(int,input().split())
tree = set()

for i in range(Q):
    num = int(input())

    temp = num
    result = [] 
    while temp:
        if temp in tree:
            result.append(temp)
        temp //=2
    
    tree.add(num)
    if result:
        ans = result[-1]
    else:
        ans = 0 
    print(ans)
        
        
    



#######################################
# import sys
# input = sys.stdin.readline
# # sys.stdin = open('input.txt')
# N, Q = map(int,input().split())

# tree =set()

# def tree_fuc(n):
#     temp = n
#     while temp >0 :
#         if temp in tree:
#             return temp
        
#         else:
#             temp //=2
#     tree.add(n)

#     return temp

# for _ in range(Q):
#     num = int(input())
    
#     print(tree_fuc(num))


    

# import sys
 
# owned = set()
# n, q = map(int, sys.stdin.readline().split())
 
# for i in range(q):
#     x = int(sys.stdin.readline())
#     node, isOwned, num = x, False, 0
#     while node > 0:
#         if node in owned:
#             isOwned = True
#             num = node
#         node //= 2
#     print(num)
#     if not isOwned:
#         owned.add(x)





