'''
'최소비용 구하기'
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = int(1e15)

N = int(input())
M = int(input())

graph = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1, c])


start, end = map(int, input().split())
start -= 1
end -= 1

answer = [INF for _ in range(N)]
answer[start] = 0
queue = []
heappush(queue, (0, start))

while queue:
    dist, node = heappop(queue)
    if dist > answer[node]:
        continue
    for i in graph[node]:
        if answer[i[0]] > dist + i[1]:
            answer[i[0]] = dist + i[1]
            heappush(queue, (answer[i[0]], i[0]))

print(answer[end])


