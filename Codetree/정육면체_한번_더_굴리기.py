# 24.04.04 16:37 ~ 17:40
from collections import deque

def round_dice(direction):
    present = dice[move_change[direction][0][0]]
    for a, b in move_change[direction]:
        present, dice[b] = dice[b], present


def cal_score(a, b):
    queue = deque()
    queue.append([a, b])
    score_board[a][b] = -1
    total = board[a][b]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            elif score_board[mx][my] == -1 or board[x][y] != board[mx][my]:
                continue
            else:
                total += board[mx][my]
                score_board[mx][my] = -1
                queue.append([mx, my])

    for i in range(n):
        for j in range(n):
            if score_board[i][j] == -1:
                score_board[i][j] = total


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

move_change = [[[5, 1], [1, 2], [2, 4], [4, 5]], [[3, 1], [1, 0], [0, 4], [4, 3]], [[2, 1], [1, 5], [5, 4], [4, 2]],
               [[0, 1], [1, 3], [3, 4], [4, 0]]]
dice = [5, 6, 4, 2, 1, 3]

score_board = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if score_board[i][j] == 0:
            cal_score(i, j)


d = 0  # 현재 진행 방향
answer = 0  # 점수
x, y = 0, 0  # 현재 위치
for i in range(m):
    x = x + dx[d]
    y = y + dy[d]

    round_dice(d)
    answer += score_board[x][y]

    if dice[1] > board[x][y]:
        d = (d + 1) % 4
    elif dice[1] < board[x][y]:
        d = (d - 1) % 4

    mx, my = x + dx[d], y + dy[d]
    if mx < 0 or mx >= n or my < 0 or my >= n:
        d = (d + 2) % 4

print(answer)
