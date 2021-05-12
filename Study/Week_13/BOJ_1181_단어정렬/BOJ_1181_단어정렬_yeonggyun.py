
N = int(input())
words = [input()for _ in range(N)]

# 받아온 단어들을 먼저 len(x) 즉 단어들의 길이만큼 순으로 정렬한다.
# 다음 인자로는 x를 넣어서 단어들 자체 적(알파벳순)으로 정렬
words.sort(key=lambda x: (len(x), x))
# 중복을 피하기 위해서 set 만듬
# 참고로 set은 순서가 무작위 이다.
temp = set()
# 단어들을 출력하기위해 반복
for word in words:
    # 만약 출력된적 없다면
    if word not in temp:
        # 기록에 저장
        temp.add(word)
        # 출력
        print(word)