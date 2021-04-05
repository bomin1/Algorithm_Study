import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # KOREA KOREA KOREA KOREAKOREAKOREA
    string = input()
    s = ''
    s += string[0]

    '''
   s = K
   i = 1 S = KO
   i = 2 S = KOR
   i = 3 S = KORE
   i = 4 S = KOREA
    '''
    for i in range(1, len(string)):
        s += string[i]
        if s == string[i+1:i+1+len(s)]:
            print("#{} {}".format(tc, len(s)))
            break

