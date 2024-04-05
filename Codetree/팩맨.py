# 24.04.05 16:52 ~ 19:50
from collections import defaultdict

def find_max(x, y, sumValue, direction):
    global maxValue, move
    if len(direction) == 3:
        if maxValue < sumValue:
            maxValue = sumValue
            move = direction
        return

    for d in range(0, 8, 2):
        mx = x + dx[d]
        my = y + dy[d]
        if 0 <= mx < 4 and 0 <= my < 4:
            if visit[mx][my] == 0:
                visit[mx][my] = 1
                count = 0
                for i in board[mx][my]:
                    count += board[mx][my][i]
                find_max(mx, my, sumValue + count, direction + [d])
                visit[mx][my] = 0
            else:
                find_max(mx, my, sumValue, direction + [d])

monster_count, t = map(int, input().split())
man_x, man_y = map(int, input().split())
man_x, man_y = man_x-1, man_y-1

board = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
for i in range(monster_count):
    x, y, d = map(int, input().split())
    board[x-1][y-1][d-1] += 1
for i in range(4):
    print(board[i])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]    # 위쪽 방향 부터 반시계 45도씩 회전
dy = [0, -1, -1, -1, 0, 1, 1, 1]
die_monster = []
for test in range(t):
    new_board = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
    not_birth = []
    # 몬스터 복제, 이동
    for i in range(4):
        for j in range(4):
            for k in board[i][j]:
                not_birth.append([i, j, k, board[i][j][k]])
                put = False
                for c in range(8):
                    d = (k + c) % 8
                    mx = i + dx[d]
                    my = j + dy[d]
                    if 0 <= mx < 4 and 0 <= my < 4 and [mx, my] != [man_x, man_y]:
                        if die_monster == []:
                            put = True
                        for dm in die_monster:
                            if [mx, my] in dm:
                                put = False
                                break
                            else:
                                put = True
                        if put:
                            new_board[mx][my][d] += board[i][j][k]
                            break
                if not put:
                    new_board[i][j][k] += board[i][j][k]

    board = new_board
    print("--복제 이동--")
    for i in range(4):
        print(board[i])


    # 팩맨 이동, 몬스터 소멸
    maxValue = -1
    move = []
    visit = [[0 for _ in range(4)] for _ in range(4)]
    visit[man_x][man_y] = 1
    find_max(man_x, man_y, 0, [])
    print("move: ", move)
    die_monster.append([])
    print(man_x ,man_y)
    for i in move:
        man_x = man_x + dx[i]
        man_y = man_y + dy[i]
        if board[man_x][man_y] != {}:
            die_monster[-1].append([man_x, man_y])
            board[man_x][man_y] = defaultdict(int)
    if len(die_monster) > 2:
        die_monster.pop(0)

    print("--팩맨이동, 소멸--")
    for i in range(4):
        print(board[i])
    print(die_monster)

    # 몬스터 복제 완성
    for x, y, d, count in not_birth:
        board[x][y][d] += count
    print("--복제끝--")
    for i in range(4):
        print(board[i])

answer = 0
for i in range(4):
    for j in range(4):
        for k in board[i][j]:
            answer += board[i][j][k]

print(answer)
