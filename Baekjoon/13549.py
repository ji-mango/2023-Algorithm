'''
'숨바꼭질 3'
'''
# 24.01.18
from collections import deque

N, K = map(int, input().split())
INF = int(1e9)

if N >= K:
    print(abs(N-K))
else:
    visit = [INF for _ in range(K * 2)]
    queue = deque([])
    queue.append([N, 0])
    visit[N] = 0
    while queue:
        location, second = queue.popleft()
        if location == K and visit[location] > second:
            visit[location] = second
            continue
        if location * 2 < K * 2 and visit[location * 2] > second and location < K:
            queue.append([location*2, second])
            visit[location*2] = second
        if location + 1 < K * 2 and visit[location + 1] > second + 1 and location < K:
            queue.append([location+1, second+1])
            visit[location + 1] = second + 1
        if location - 1 >= 0 and visit[location - 1] > second + 1:
            queue.append([location-1, second+1])
            visit[location - 1] = second + 1

    print(visit[K])


