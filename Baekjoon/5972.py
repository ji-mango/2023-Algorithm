'''
'택배 배송'
'''
# 24.01.26 16:03 ~ 16:40
# from collections import deque
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# N, M = map(int, input().split())
# edges = [[] for _ in range(N+1)]
#
# for i in range(M):
#     a, b, c = map(int, input().split())
#     edges[a].append([b, c])
#     edges[b].append([a, c])
#
# answer = [INF for _ in range(N+1)]
# answer[1] = 0
#
# queue = deque()
# queue.append(1)
#
# while queue:
#     node = queue.popleft()
#     for next, amount in edges[node]:
#         if answer[next] > answer[node] + amount:
#             queue.append(next)
#             answer[next] = min(answer[next], answer[node] + amount)
#
#
# print(answer[N])

# 24.01.26 수정(개선된 다익스트라 : 우선순위큐를 이용해 거리가 짧은 것 부터 큐에서 먼저 빼기)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

answer = [INF for _ in range(N+1)]
answer[1] = 0

queue = []
heapq.heappush(queue, (0, 1))

while queue:
    distance, node = heapq.heappop(queue)
    for next, amount in edges[node]:
        if answer[next] > answer[node] + amount:
            heapq.heappush(queue, (distance + amount, next))
            answer[next] = distance + amount


print(answer[N])
