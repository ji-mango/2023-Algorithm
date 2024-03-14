'''
'벽 부수고 이동하기'
'''

# 24.03.14 14:56 ~ 16:03
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().strip())))

record = []
for i in range(N):
    record.append([[INF, INF] for _ in range(M)])
record[0][0] = [1, 1]

queue = deque()
queue.append([[0, 0], 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    [x, y], hit = queue.popleft()
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= N or my < 0 or my >= M:
            continue
        if board[mx][my] == 1:
            if hit == 1:
                continue
            elif record[mx][my][1] > record[x][y][0] + 1:
                record[mx][my][1] = record[x][y][0] + 1
                queue.append([[mx, my], hit+1])
        else:
            if record[mx][my][hit] > record[x][y][hit] + 1:
                record[mx][my][hit] = record[x][y][hit] + 1
                queue.append([[mx, my], hit])

answer = min(record[-1][-1])
if answer == INF:
    print(-1)
else:
    print(answer)

