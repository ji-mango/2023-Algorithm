'''
'불!"
'''
# 24.02.16 14:46 ~ 15:58
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

R, C = map(int, input().split())

board = []
J = deque()
fire = deque()
for i in range(R):
    board.append(list(input().strip()))
    for j in range(C):
        if board[i][j] == 'F':
            fire.append([i, j])
        elif board[i][j] == 'J':
            J.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
visit = [[INF for _ in range(C)] for _ in range(R)]     # 지훈이의 방문 표시
visit[J[0][0]][J[0][1]] = 0

def move():
    while True:
        if len(J) == 0:             # 지훈이가 없으면 IMPOSSIBLE 출력
            return "IMPOSSIBLE"

        length = len(fire)
        for i in range(length):     # 불 확산(기존 큐 길이만큼만 반복)
            x, y = fire.popleft()
            for j in range(4):
                mx = x + dx[j]
                my = y + dy[j]
                if mx < 0 or mx >= R or my < 0 or my >= C or board[mx][my] == '#' or board[mx][my] == 'F':
                    continue
                else:
                    board[mx][my] = 'F'     # 확산된 불은 바로 F로 바꾸어주어 중복으로 불이 큐에 들어가는 일이 없도록함
                    fire.append([mx, my])

        length = len(J)
        for i in range(length):     # 지훈이 이동(기존 큐 길이만큼만 반복)
            x, y = J.popleft()
            for j in range(4):
                mx = x + dx[j]
                my = y + dy[j]
                if mx < 0 or mx >= R or my < 0 or my >= C:  # 지훈이가 빠져나갈 수 있는 경우 return
                    return visit[x][y] + 1
                elif board[mx][my] == 'F' or board[mx][my] == '#' or visit[mx][my] <= visit[x][y] + 1:  # 이전 지훈이의 이동수보다 더 많은 이동이 필요한 경우에도 continue
                    continue
                else:
                    visit[mx][my] = visit[x][y] + 1
                    J.append([mx, my])

print(move())
