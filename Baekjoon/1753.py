'''
'최단경로'
'''
# 24.02.15 16:28 ~
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input()) - 1

graph = [[] for _ in range(V)]
answer = [INF] * V
answer[K] = 0

for i in range(E):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1

    graph[u].append([v, w])

queue = [[0, K]]
while queue:
    distance, node = heapq.heappop(queue)

    for v, w in graph[node]:
        if distance + w < answer[v]:
            answer[v] = distance + w
            heapq.heappush(queue, [distance+w, v])

for i in answer:
    if i == INF:
        print("INF")
    else:
        print(i)
