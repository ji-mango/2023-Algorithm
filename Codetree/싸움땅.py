# 24.04.13 15:02 ~ 17:09
def loser_move(number):
    x, y, d, s, gun, point = player[number]
    if gun != 0:
        board[x][y].append(gun)
        player[number][4] = 0
        d

    for i in range(4):
        mx = x + dx[d]
        my = y + dy[d]

        if mx < 0 or mx >= N or my < 0 or my >= N or player_board[mx][my] != []:
            d = (d + 1) % 4
        else:
            break

    player[number][0], player[number][1] = mx, my
    player[number][2] = d
    player_board[x][y].remove(number)
    player_board[mx][my].append(number)


    choose_gun(number)


def choose_gun(number):
    x, y, d, s, gun, point = player[number]
    max_gun = gun
    for g in board[x][y]:
        if g > max_gun:
            max_gun = g

    if max_gun > gun:
        board[x][y].remove(max_gun)
        if gun != 0:
            board[x][y].append(gun)
        player[number][4] = max_gun



N, M, K = map(int, input().split())

board = []
for i in range(N):
    gun = list(map(int, input().split()))
    board.append([])
    for j in range(N):
        if gun[j] == 0:
            board[i].append([])
        else:
            board[i].append([gun[j]])


player = []
player_board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y, d, s = map(int, input().split())
    player.append([x-1, y-1, d, s, 0, 0])
    player_board[x-1][y-1].append(i)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for k in range(K):
    print("round", k)
    for p in range(M):
        # 플레이어 이동
        x, y, d, s, gun, point = player[p]
        mx = x + dx[d]
        my = y + dy[d]

        if mx < 0 or mx >= N or my < 0 or my >= N:
            d = (d + 2) % 4
            mx = x + dx[d]
            my = y + dy[d]

        player[p][0], player[p][1] = mx, my
        player_board[mx][my].append(p)
        player_board[x][y].pop(0)
        player[p][2] = d

        print("플레이어 이동 후")
        for i in range(N):
            print(board[i])
        print("player: ", player)
        for i in range(N):
            print(player_board[i])

        # 이동 칸에 플레이어가 없고 총이 있다면
        if len(player_board[mx][my]) == 1:
            choose_gun(p)
            print("대결x, 총만가져간 후")
            for i in range(N):
                print(board[i])
            print("player: ", player)
            for i in range(N):
                print(player_board[i])

        # 이동 칸에 플레이어가 있는 경우
        else:
            other = player_board[mx][my][0]
            winner = -1
            loser = -1

            if gun + s > player[other][3] + player[other][4]:
                winner = p
                loser = other
            elif gun + s < player[other][3] + player[other][4]:
                winner = other
                loser = p
            else:
                if s > player[other][3]:
                    winner = p
                    loser = other
                else:
                    winner = other
                    loser = p

            print("winner: ", winner, "loser:", loser)
            player[winner][5] += abs((gun + s) - (player[other][3] + player[other][4]))
            loser_move(loser)
            choose_gun(winner)

            print("대결 후")
            for i in range(N):
                print(board[i])
            print("player: ", player)
            for i in range(N):
                print(player_board[i])
    print()


for i in range(M):
    print(player[i][-1], end = ' ')
