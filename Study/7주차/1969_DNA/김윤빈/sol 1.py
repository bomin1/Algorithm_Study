"""
순열 전부다 구해서
갯수 가장 작을때 순열 찾기
4개의 단어로 8개단어 순열 조합 만드는 법?
permutations 안되네
"""
# import sys

# input = sys.stdin.readline

N, M = map(int, input().split())

words = []
# 각라인마다 가장 많은 숫자 카운트,

result = 0
w = [list(input()) for _ in range(N)]
for i in range(M):
    word = {'A': 0, 'C': 0, 'G': 0, 'T': 0} # 와 ㅡㅡ 무슨 dna가 같으면 사전순 ;;;;;;  a,c,g,t 순으로 안하면 틀림 ㄷ
    for j in range(N):
        word[w[j][i]] += 1
    # print(word) {'A': 1, 'T': 1, 'G': 1, 'C': 1}
    '''
    최대 value값에 대한 key값 찾기 
    max(word)를 하면 word의 key 값중 최대값으로 T만 나옴
    key = word.get > key입력으로 value를 출력해주는 함수. 
    https://bio-info.tistory.com/40
    '''
    temp = max(word, key=word.get)
    words.append(temp)
    result += (N - word.get(temp))

print(''.join(words))

print(result)
