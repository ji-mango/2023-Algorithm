'''
'비슷한 단어'
'''
# 24.02.22 14:59 ~
import sys
input = sys.stdin.readline


def compare(a, b):
    length = 0
    index = 0
    for i in a:
        if index < len(b) and i == b[index]:
            length += 1
        else:
            break
        index += 1
    return length


N = int(input())

word_list = []
for i in range(N):
    word_list.append([input().strip(), i])

words = sorted(word_list)

length = [0] * (N+1)
max_length = 0

for i in range(N - 1):
    compare_length = compare(words[i][0], words[i + 1][0])
    max_length = max(max_length, compare_length)

    length[words[i][1]] = max(length[words[i][1]], compare_length)
    length[words[i + 1][1]] = max(length[words[i + 1][1]], compare_length)

first = 0
for i in range(N):
    if first == 0:
        if length[i] == max(length):
            first = word_list[i][0]
            print(first)
            before = word_list[i][0][:max_length]
    else:
        if length[i] == max(length) and word_list[i][0][:max_length] == before:
            print(word_list[i][0])
            break
