# 24.04.12 20:15 ~ 22:45
from collections import deque

def find_max_min():
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                if (board[i][j] < min_top[0]) \
                        or (board[i][j] == min_top[0] and record[i][j] > record[min_top[1][0]][min_top[1][1]]) \
                        or (board[i][j] == min_top[0] and record[i][j] == record[min_top[1][0]][min_top[1][1]] and (i+j) > sum(min_top[1])) \
                        or (board[i][j] == min_top[0] and record[i][j] == record[min_top[1][0]][min_top[1][1]] and (i+j) == sum(min_top[1]) and j > min_top[1][1]):
                    min_top[0] = board[i][j]
                    min_top[1] = [i, j]
                if (board[i][j] > max_top[0]) \
                        or (board[i][j] == max_top[0] and record[i][j] < record[max_top[1][0]][max_top[1][1]]) \
                        or (board[i][j] == max_top[0] and record[i][j] == record[max_top[1][0]][max_top[1][1]] and (i+j) < sum(max_top[1])) \
                        or (board[i][j] == max_top[0] and record[i][j] == record[max_top[1][0]][max_top[1][1]] and (i+j) == sum(max_top[1]) and j < max_top[1][1]):
                    max_top[0] = board[i][j]
                    max_top[1] = [i, j]


def laser(x, y, damage):
    success = 0
    queue = deque()
    queue.append([x, y])
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[x][y] = -1
    damage_board = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = (x + ldx[i]) % N
            my = (y + ldy[i]) % M

            if [mx, my] == max_top[1]:
                visit[mx][my] = [x, y]
                damage_board[mx][my] = 1
                success = 1
                break

            if visit[mx][my] == 0 and board[mx][my] != 0:
                visit[mx][my] = [x, y]
                queue.append([mx, my])
        if success == 1:
            break
    for i in range(N):
        print(visit[i])
    if success == 1:
        print("레이저공격")
        present = max_top[1]
        board[present[0]][present[1]] -= damage
        if board[present[0]][present[1]] < 0:
            board[present[0]][present[1]] = 0

        damage = damage // 2
        while True:
            present = visit[present[0]][present[1]]
            damage_board[present[0]][present[1]] = 1
            if present == min_top[1]:
                break

            board[present[0]][present[1]] -= damage
            if board[present[0]][present[1]] < 0:
                board[present[0]][present[1]] = 0

        print("공격 후 board")
        for i in range(N):
            print(board[i])

        for i in range(N):
            for j in range(M):
                if damage_board[i][j] == 0 and board[i][j] != 0:
                    board[i][j] += 1
    return success


def bomb(x, y, damage):
    print("포탄 공격")
    present = max_top[1]
    board[present[0]][present[1]] -= damage
    if board[present[0]][present[1]] < 0:
        board[present[0]][present[1]] = 0
    damage_board = [[0 for _ in range(M)] for _ in range(N)]
    damage_board[present[0]][present[1]] = 1
    damage_board[x][y] = 1

    damage = damage // 2
    for i in range(8):
        mx = (present[0] + bdx[i]) % N
        my = (present[1] + bdy[i]) % M

        if [mx, my] == [x, y] or [mx + N, my] == [x, y] or [mx, my + M] == [x, y] or [mx + N, my + M] == [x, y] or board[mx][my] == 0:
            continue
        board[mx][my] -= damage
        if board[mx][my] < 0:
            board[mx][my] = 0
        damage_board[mx][my] = 1
    print("공격 후 board")
    for i in range(N):
        print(board[i])

    for i in range(N):
        for j in range(M):
            if damage_board[i][j] == 0 and board[i][j] != 0:
                board[i][j] += 1


N, M, K = map(int, input().split())
INF = int(1e9)

board = []
for i in range(N):
    board.append(list(map(int, input().split())))
record = [[0 for _ in range(M)] for _ in range(N)]




ldx = [0, 1, 0, -1]     # 우, 하, 좌, 상
ldy = [1, 0, -1, 0]

bdx = [-1, -1, -1, 0, 0, 1, 1, 1]
bdy = [-1, 0, 1, -1, 1, -1, 0, 1]

for k in range(K):
    min_top = [INF, [-1, -1]]
    max_top = [0, [-1, -1]]
    find_max_min()
    print("min, max: ", min_top, max_top)
    min_x, min_y = min_top[1]
    record[min_x][min_y] = k+1
    board[min_x][min_y] += (N + M)

    if not laser(min_x, min_y, board[min_x][min_y]):
        bomb(min_x, min_y, board[min_x][min_y])
    print("정비 후 board")
    for i in range(N):
        print(board[i])

    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                count += 1

    if count == 1:
        break

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, board[i][j])

print(answer)

