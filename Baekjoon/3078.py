'''
'좋은 친구'
'''
# 24.01.31 16:30 ~ 17:34
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
names = []
for i in range(N):
    names.append(input().strip())

answer = 0
count = defaultdict(int)
queue = deque()

K = min(N-1, K)
for i in range(K+1):
    length = len(names[i])
    queue.append(length)
    count[length] += 1
    if count[length] >= 2:
        answer += count[length] - 1


for i in range(K+1, N):
    pop = queue.popleft()
    count[pop] -= 1

    length = len(names[i])
    queue.append(length)
    count[length] += 1
    if count[length] >= 2:
        answer += count[length] - 1

print(answer)
