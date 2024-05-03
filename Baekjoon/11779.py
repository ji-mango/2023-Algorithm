'''
'최소비용 구하기2'
'''

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = int(1e15)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())
road = [[] for _ in range(n+1)]
road[start] = [start]

distance = [INF for _ in range(n+1)]
distance[start] = 0
queue = []
heappush(queue, (0, start))

while queue:
    dist, node = heappop(queue)
    if dist > distance[node]:
        continue
    for i in graph[node]:
        cost = i[1] + distance[node]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            road[i[0]] = road[node] + [i[0]]
            heappush(queue, (cost, i[0]))

print(distance[end])
print(len(road[end]))
print(*road[end])

