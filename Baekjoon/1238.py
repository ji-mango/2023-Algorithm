'''
'파티'
'''
# 24.02.24 16:49 ~ 17:36
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dik(i, end):
    queue = []
    distance = [INF for _ in range(N + 1)]
    distance[i] = 0
    visit = [0 for _ in range(N + 1)]
    visit[i] = 1

    for node, dist in graph[i]:
        distance[node] = dist
        heapq.heappush(queue, [dist, node])

    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:                                 # 방문한 노드가 목표 노드라면 함수 종료
            return distance

        visit[node] = 1
        for next, next_dist in graph[node]:
            if visit[next] == 1:
                continue
            if next_dist + distance[node] < distance[next]:
                distance[next] = next_dist + distance[node]
                heapq.heappush(queue, [distance[next], next])
    return distance


N, M , X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

answer = 0
base_distance = dik(X, 2000)                            # X노드는 모든 노드와의 거리를 계산해야 하기 때문에 두번째 인자에 큰 값을 넣어줌
for i in range(1, N+1):
    distance = dik(i, X)
    answer = max(answer, base_distance[i] + distance[X])

print(answer)
