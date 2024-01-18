'''
'회전 초밥'
'''
# 24.01.18
from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
plate = []
for i in range(N):
    plate.append(int(input()))

answer = 0
length = 0
visit = defaultdict(int)

for i in range(k):
    visit[plate[i]] += 1

answer = len(visit)
length = answer

if visit[c] == 0:
    answer += 1

left = 0
right = k
while True:
    visit[plate[left]] -= 1
    if visit[plate[left]] == 0:
        length -= 1
    if visit[plate[right]] == 0:
        length += 1
    visit[plate[right]] += 1
    if visit[c] == 0:
        answer = max(answer, length + 1)
    else:
        answer = max(answer, length)
    if right == k-1:
        break

    left = (left+1) % N
    right = (right+1) % N

print(answer)
