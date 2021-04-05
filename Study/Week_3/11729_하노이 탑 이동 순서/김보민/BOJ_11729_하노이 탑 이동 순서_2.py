def get_idx(n,r,c):
    if n == 0:
        return 0
    half = 2 ** (n-1) # 4
    if r < half and c < half:
        return get_idx(n-1,r,c)
    if c >= half and r < half:
        return half * half + get_idx(n-1, r, c-half)
    if r >= half and c < half:
        return 2 * half * half + get_idx(n-1, r-half, c)
    return 3 * half * half + get_idx(n-1, r-half, c-half)

n, r, c = 3,7,7
print(get_idx(n,r,c))