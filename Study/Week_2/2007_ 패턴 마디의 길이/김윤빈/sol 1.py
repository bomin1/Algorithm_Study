import sys

sys.stdin = open('input.txt')

tc = int(input())

for tc in range(1, tc + 1):
    word = input()

    word_list = []
    # 마디의 최대 길이는 10이므로
    #['K', 'KO', 'KOR', 'KORE', 'KOREA', 'KOREAK', 'KOREAKO', 'KOREAKOR', 'KOREAKORE', 'KOREAKOREA']
    for i in range(1, 11):
        word_list.append(word[:i])

    for i in range(10):
        # 1. korea 뒤에 korea가 있는지 체크
        # 2. koreakorea 일 경우를 제외
        if word_list[i] == word[len(word_list[i]): 2 * len(word_list[i])] and len(word_list[i]) < 10:
            print("#{} {}".format(tc, len(word_list[i])))
            break
