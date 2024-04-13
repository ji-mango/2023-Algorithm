# 24.04.13 17:30 ~ 18:49 + 20:08 ~ 22:52
from collections import deque

def move(a, b):
    x, y = a, b
    present = board[x][y]
    while True:
        check = 0
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < N and 0 <= my < N and board[mx][my] == 2 and visit[mx][my] == 0:
                board[mx][my], present = present, board[mx][my]
                visit[mx][my] = 1
                x, y = mx, my
                check = 1
                break

        if check == 0:
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx < N and 0 <= my < N and board[mx][my] == 1 and visit[mx][my] == 0:
                    board[mx][my], present = present, board[mx][my]
                    visit[mx][my] = 1
                    x, y = mx, my
                    break

            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx < N and 0 <= my < N:
                    if board[mx][my] == 4 and visit[mx][my] == 0:
                        board[mx][my] = present
                        board[a][b] = 4
                    elif board[mx][my] == 3 and visit[mx][my] == 0:
                        board[mx][my] = present
            break


def throw_ball(x, y, d):
    score = 0
    while 0 <= x < N and 0 <= y < N:
        if board[x][y] != 0 and board[x][y] != 4:
            print("공맞은애 : ", x, y)
            queue = deque()
            visit = [[0 for _ in range(N)] for _ in range(N)]
            visit[x][y] = 1
            head = [-1, -1]
            tail = [-1, -1]
            queue.append([x, y, 1])
            while queue:
                x, y, count = queue.popleft()
                if board[x][y] == 1:
                    score = count
                    print('점수', count)
                    head = [x, y]

                elif board[x][y] == 3:
                    tail = [x, y]

                for i in range(4):
                    mx = x + dx[i]
                    my = y + dy[i]
                    if 0 <= mx < N and 0 <= my < N and board[mx][my] != 4 and board[mx][my] != 0 and visit[mx][my] == 0:
                        if (board[x][y] == 3 and board[mx][my] == 1) or (board[x][y] == 1 and board[mx][my] == 3):
                            continue
                        queue.append([mx, my, count+1])
                        visit[mx][my] = 1
            print("head, tail", head, tail)
            board[tail[0]][tail[1]], board[head[0]][head[1]] = 1, 3
            break
        x = x + dx[d]
        y = y + dy[d]
    return score


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())

board = []
head = [[-1, -1] for _ in range(M)]
tail = [[-1, -1] for _ in range(M)]
for i in range(N):
    board.append(list(map(int, input().split())))

ball_start = [0, 0]
answer = 0
for k in range(K):
    d = (k // N) % 4
    if k % N != 0:
        if d == 0:
            ball_start[0] += 1
        elif d == 1:
            ball_start[1] += 1
        elif d == 2:
            ball_start[0] -= 1
        else:
            ball_start[1] -= 1

    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 3 and visit[i][j] == 0:
                move(i, j)
    print("이동 후")
    for _ in range(N):
        print(board[_])

    print("방향, 시작", d, ball_start)
    answer += (throw_ball(ball_start[0], ball_start[1], d)) ** 2
    print("볼 던진 후")
    for _ in range(N):
        print(board[_])
    print(answer)
    print()

print(answer)
