'''
'비슷한 단어'
'''
# 24.01.12
from collections import defaultdict

N = int(input())
word = input()
word_dict = defaultdict(int)
for i in word:
    word_dict[i] += 1

answer = 0
for i in range(N-1):
    compare = input()
    compare_dict = defaultdict(int)
    length_compare = abs(len(compare) - len(word))

    if length_compare > 1:
        continue
    for j in compare:
        compare_dict[j] += 1

    if length_compare == 1:
        result = 0
        if len(compare) > len(word):
            for j in word_dict:
                if j not in compare_dict:
                    result = 1
                    break
                elif compare_dict[j] < word_dict[j]:
                    result = 1
                    break

        elif len(word) > len(compare):
            for j in compare_dict:
                if j not in word_dict:
                    result = 1
                    break
                elif compare_dict[j] > word_dict[j]:
                    result = 1
                    break

        if result == 0:
            answer += 1

    else:
        different1 = 0
        different2 = 0
        for j in compare_dict:
            if j not in word_dict:
                different1 += compare_dict[j]
            else:
                different2 += abs(compare_dict[j] - word_dict[j])
        if different1 >=2:
            continue
        elif different2 > 2:
            continue

        different3 = 0
        different4 = 0
        for j in word_dict:
            if j not in compare_dict:
                different3 += word_dict[j]
            else:
                different4 += abs(word_dict[j] - compare_dict[j])

        if different3 >= 2:
            continue
        elif different4 > 2:
            continue

        answer += 1
print(answer)
