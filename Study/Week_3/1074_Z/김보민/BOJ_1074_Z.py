def z(n,r,c):
    if n == 0:
        return 0
    # 크게 사등분 해야하니까
    n_half = 2**(n-1)
    '''
    12
    34
    '''
    # 2^(n-1)영역에서 방문해야하니까 n-1로접근
    # 1영역(0 1 2 3)
    if r < n_half and c < n_half:
        return z(n-1,r,c)
    # 2 영역(4 5 6 7)
    elif r < n_half and c >= n_half:
        return n*n + z(n-1,r,c-n_half)
    # 3영역(8 9 10 11)
    elif r >= n_half and c < n_half:
        return 2*n*n + z(n-1,r-n_half,c)
    # 4영역 (12 13 14 15)
    else:
        return 3*n*n + z(n-1,r-n_half,c-n_half)



