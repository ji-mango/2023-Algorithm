def red_remove():
    global score
    y = 5
    while y >= 2:
        isRemove = 1
        for i in range(4):
            if red_board[i][y] == 0:
                isRemove = 0
                break
        if isRemove:
            score += 1
            for i in range(4):
                for j in range(y-1, -1, -1):
                    red_board[i][j], red_board[i][j+1] = 0, red_board[i][j]
        else:
            y -= 1
    for a in range(4):
        if red_board[a][0] == 1:
            for i in range(4):
                for j in range(3, -1, -1):
                    red_board[i][j], red_board[i][j + 2] = 0, red_board[i][j]
            break

    for a in range(4):
        if red_board[a][1] == 1:
            for i in range(4):
                for j in range(4, -1, -1):
                    red_board[i][j], red_board[i][j + 1] = 0, red_board[i][j]
            break


def yellow_remove():
    global score
    x = 5
    while x >= 2:
        isRemove = 1
        for i in range(4):
            if yellow_board[x][i] == 0:
                isRemove = 0
                break

        if isRemove:
            score += 1
            for j in range(x - 1, -1, -1):
                yellow_board[j], yellow_board[j+1] = [0, 0, 0, 0], yellow_board[j]
        else:
            x -= 1

    for i in range(4):
        if yellow_board[0][i] == 1:
            for j in range(3, -1, -1):
                yellow_board[j], yellow_board[j+2] = [0, 0, 0, 0], yellow_board[j]
            break

    for i in range(4):
        if yellow_board[1][i] == 1:
            for j in range(4, -1, -1):
                yellow_board[j], yellow_board[j+1] = [0, 0, 0, 0], yellow_board[j]
            break


def red_go(shape):
    red = 1
    while True:
        new_shape = [[x, y] for x, y in shape]
        for i in range(len(shape)):
            mx = shape[i][0] + dx[0]
            my = shape[i][1] + dy[0]
            if my > 5:
                red = 0
                break
            if red_board[mx][my] != 0:
                red = 0
                break
            new_shape[i][0], new_shape[i][1] = mx, my
        if red == 0:
            break
        shape = new_shape

    for x, y in shape:
        red_board[x][y] = 1
    red_remove()


def yellow_go(shape):
    yellow = 1
    while True:
        new_shape = [[x, y] for x, y in shape]
        for i in range(len(shape)):
            mx = shape[i][0] + dx[1]
            my = shape[i][1] + dy[1]
            if mx > 5:
                yellow = 0
                break
            if yellow_board[mx][my] != 0:
                yellow = 0
                break
            new_shape[i][0], new_shape[i][1] = mx, my
        if yellow == 0:
            break
        shape = new_shape

    for x, y in shape:
        yellow_board[x][y] = 1
    yellow_remove()


k = int(input())

score = 0
red_board = [[0 for _ in range(6)] for _ in range(4)]
yellow_board = [[0 for _ in range(4)] for _ in range(6)]

dx = [0, 1]  # red, yellow
dy = [1, 0]


for i in range(k):
    t, x, y = map(int, input().split())
    if t == 1:
        red_go([[x, 0]])
        yellow_go([[0, y]])
    elif t == 2:
        red_go([[x, 1], [x, 0]])
        yellow_go([[0, y], [0, y+1]])
    else:
        red_go([[x, 0], [x+1, 0]])
        yellow_go([[1, y], [0, y]])

count = 0
for i in range(4):
    for j in range(2, 6):
        if red_board[i][j] == 1:
            count += 1

for i in range(2, 6):
    for j in range(4):
        if yellow_board[i][j] == 1:
            count += 1

print(score)
print(count)
