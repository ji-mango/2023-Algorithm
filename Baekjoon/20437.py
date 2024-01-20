'''
'문자열 게임 2'
'''
# 24.01.20
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    word = input().strip()
    K = int(input())

    if K == 1:
        print(1, 1)
        continue

    visit = [0 for _ in range(26)]
    length = set()

    for j in range(len(word)):
        w = word[j]

        if visit[ord(w)-97] == 1:
            continue

        visit[ord(w)-97] = 1
        record = deque([j])

        for k in range(j+1, len(word)):
            if word[k] == w:
                record.append(k)
                if len(record) == K:
                    length.add(k-record[0]+1)
                    record.popleft()

    if length:
        print(min(length), max(length))
    else:
        print(-1)

