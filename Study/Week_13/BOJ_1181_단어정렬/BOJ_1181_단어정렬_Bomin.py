import sys
sys.stdin = open("input.txt")

n = int(input())
word_info = {}
for i in range(n):
    word = input()
    word_info[word] = len(word)
print(word_info)
# {'but': 3, 'i': 1, 'wont': 4, 'hesitate': 8, 'no': 2, 'more': 4, 'it': 2, 'cannot': 6, 'wait': 4, 'im': 2, 'yours': 5}
sorted_word_info = sorted(word_info.items(), key=lambda x: (x[1], x[0]))
print(sorted_word_info)
# [('i', 1), ('im', 2), ('it', 2), ('no', 2), ('but', 3), ('more', 4), ('wait', 4), ('wont', 4), ('yours', 5), ('cannot', 6), ('hesitate', 8)]

for word, length in sorted_word_info:
    print(word)

