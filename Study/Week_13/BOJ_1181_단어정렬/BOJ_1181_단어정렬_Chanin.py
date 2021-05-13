sys

T = 1

# 1. 일차적으로 set으로 중복제거
# 2. 버블정렬로 길이순
# 3. 같으면 사전순서대로 정렬

dictionary_order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for tc in range(1, T+1):
    N = int(input())
    word_list = []
    for i in range(N):
        word_list += [input()]
    # print(word_list)
    # ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

    word_list = set(word_list)
    word_list = list(word_list) # 셋으로 바꿨다가 돌려서 중복되는 단어 삭제

    for i in range(len(word_list)-1,-1,-1): # 우선 버블솔트를 통해서 정렬
        for j in range(0,i):
            if len(word_list[j]) > len(word_list[j+1]):
                word_list[j], word_list[j+1] = word_list[j+1], word_list[j]


    print(word_list)
    # ['i', 'it', 'im', 'no', 'but', 'wait', 'more', 'wont', 'yours', 'cannot', 'hesitate']

    for j in range(0,len(word_list)-1):
        if len(word_list[j]) == len(word_list[j+1]): # 길이가 같은걸 만나면
            for k in range(len(word_list[j])): # 해당 글자의 한 글자씩 반복
                if dictionary_order.index(word_list[j][k],0) < dictionary_order.index(word_list[j+1][k],0): # 앞에꺼가 사전순서상 잘 앞에 있는거라면 (인덱스가 더 작다면)
                    break #그대로 두고
                elif dictionary_order.index(word_list[j][k],0) > dictionary_order.index(word_list[j+1][k],0): # 아니면 (사전상 더 뒤에있다면) 순서도 뒤로 보내라
                        word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]

    print(*word_list, sep='\n')

    # 왜 출력 할때마다 달라짐?






