'''
'녹색 옷 입은 애가 젤다지?'
'''
# 24.02.06 15:32 ~ 15:52
import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

problem = 1
while True:
    N = int(input())
    if N == 0:
        break

    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    queue = deque()
    queue.append([0, 0])

    answer_board = [[INF for _ in range(N)] for _ in range(N)]
    answer_board[0][0] = board[0][0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= N or my < 0 or my >= N or answer_board[mx][my] <= answer_board[x][y] + board[mx][my]:
                continue
            else:
                answer_board[mx][my] = answer_board[x][y] + board[mx][my]
                if [mx, my] != [N-1, N-1]:
                    queue.append([mx, my])

    print("Problem "+str(problem)+":", answer_board[N-1][N-1])
    problem += 1
