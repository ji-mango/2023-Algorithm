# 24.04.08 14:30 ~ 18:40
import sys
input = sys.stdin.readline

n, m, h, k = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(n)]
tree = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]   # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

tagger_x, tagger_y = n//2, n//2
tagger_d = [0, 1]  # [방향, 달팽이 진행 방향]

for i in range(m):
    x, y, d = map(int, input().split())
    board[x-1][y-1].append(d)

for i in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = 1

answer = 0

for t in range(1, k+1):
    # 도망자 이동
    new_board = []
    for i in range(n):
        new_board.append([])
        for j in range(n):
            new_board[i].append([])
            for k in board[i][j]:
                new_board[i][j].append(k)

    for i in range(tagger_x - 3, tagger_x + 4):
        for j in range(tagger_y - 3, tagger_y + 4):
            if i < 0 or i >= n or j < 0 or j >= n or (abs(i-tagger_x) + abs(j-tagger_y) > 3):
                continue
            for r in board[i][j]:
                new_board[i][j].pop(0)
                d = r
                mx = i + dx[d]
                my = j + dy[d]
                if mx < 0 or mx >= n or my < 0 or my >= n:
                    d = (d + 2) % 4
                    mx = i + dx[d]
                    my = j + dy[d]

                if [mx, my] != [tagger_x, tagger_y]:
                    new_board[mx][my].append(d)
                else:
                    new_board[i][j].append(d)
    board = new_board

    # 술래 이동
    tagger_x = tagger_x + dx[tagger_d[0]]
    tagger_y = tagger_y + dy[tagger_d[0]]

    if [tagger_x, tagger_y] == [0, 0]:
        tagger_d = [2, -1]
    elif [tagger_x, tagger_y] == [n//2, n//2]:
        tagger_d = [0, 1]
    elif (abs(n//2 - tagger_x) == abs(n//2 - tagger_y) and not(tagger_x < n//2 and tagger_y < n//2)) or (abs(n//2 - tagger_x) == abs(n//2 - (tagger_y-1)) and (n//2 - tagger_x) > 0 and (n//2 - (tagger_y-1)) > 0):
        tagger_d[0] = (tagger_d[0] + tagger_d[1]) % 4


    kill_x, kill_y = tagger_x, tagger_y
    for i in range(3):
        if kill_x < 0 or kill_x >= n or kill_y < 0 or kill_y >= n:
            break
        if tree[kill_x][kill_y] == 0:
            answer += t * len(board[kill_x][kill_y])
            board[kill_x][kill_y] = []

        kill_x = kill_x + dx[tagger_d[0]]
        kill_y = kill_y + dy[tagger_d[0]]


print(answer)


