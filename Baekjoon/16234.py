'''
'인구 이동'
'''
# 24.01.29 16:05 ~ 16:48
from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
while True:
    average = []
    average_index = 0
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1:
                average.append([board[i][j], 1])
                queue = deque()
                queue.append([i, j])
                visit[i][j] = average_index
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        mx = dx[d] + x
                        my = dy[d] + y
                        if mx < 0 or mx >= N or my < 0 or my >= N or visit[mx][my] != -1:
                            continue
                        elif L <= abs(board[mx][my]-board[x][y]) <= R:
                            queue.append([mx, my])
                            average[average_index][0] += board[mx][my]
                            average[average_index][1] += 1
                            visit[mx][my] = average_index
                average_index += 1

    if average_index == N * N:
        break
    for i in range(N):
        for j in range(N):
            if visit[i][j] != -1:
                board[i][j] = average[visit[i][j]][0] // average[visit[i][j]][1]
    answer += 1

print(answer)
