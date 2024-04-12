# 24.04.11
import sys
input = sys.stdin.readline

def move_people():
    global board
    count = 0
    new_board = []
    for i in range(N):
        new_board.append([])
        for j in range(N):
            new_board[i].append([board[i][j]])

    for i in range(N):
        for j in range(N):
            if board[i][j] < 0:
                x, y = i, j
                if outdoor[0] > x and outdoor[1] > y:
                    direction = [1, 3]
                elif outdoor[0] > x and outdoor[1] == y:
                    direction = [1]
                elif outdoor[0] > x and outdoor[1] < y:
                    direction = [1, 2]
                elif outdoor[0] == x and outdoor[1] > y:
                    direction = [3]
                elif outdoor[0] == x and outdoor[1] < y:
                    direction = [2]
                elif outdoor[0] < x and outdoor[1] > y:
                    direction = [0, 3]
                elif outdoor[0] < x and outdoor[1] == y:
                    direction = [0]
                elif outdoor[0] < x and outdoor[1] < y:
                    direction = [0, 2]

                for d in direction:
                    mx = x + dx[d]
                    my = y + dy[d]
                    if board[mx][my] <= 0 or board[mx][my] == 10:
                        count += abs(board[x][y])
                        if board[mx][my] <= 0:
                            new_board[mx][my].append(board[x][y])
                        new_board[x][y].pop(0)
                        break
    for i in range(N):
        for j in range(N):
            board[i][j] = sum(new_board[i][j])
    return count

def find_square():
    size = 2
    is_person, is_outdoor = 0, 0

    for i in range(N-1, 0, -1):
        for x in range(i):
            for y in range(i):
                for r in range(x, x+size):
                    for c in range(y, y+size):
                        if board[r][c] < 0:
                            is_person = 1
                        if board[r][c] == 10:
                            is_outdoor = 1

                        if is_person and is_outdoor:
                            return x, y, size
                is_person, is_outdoor = 0, 0
        size += 1
    return 0,0,0

def rotate(x, y, size):
    new_square = [[0 for _ in range(N)] for _ in range(N)]
    index_x = x
    for i in range(y, y+size):
        new_square.append([])
        index_y = y
        for j in range(x+size-1, x-1, -1):
            new_square[index_x][index_y] = board[j][i]
            if board[j][i] > 0 and board[j][i] != 10:
                new_square[index_x][index_y] -= 1
            index_y += 1
        index_x += 1

    for i in range(x, x+size):
        for j in range(y, y+size):
            board[i][j] = new_square[i][j]


N, M, K = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

for i in range(M):
    x, y = map(int, input().split())
    board[x-1][y-1] -= 1

temp_x, temp_y = map(int, input().split())
outdoor = [temp_x-1, temp_y-1]
board[temp_x-1][temp_y-1] = 10

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

move_count = 0
for i in range(N):
    print(board[i])

for i in range(K):
    move_count += move_people()
    print("사람이동")
    for x in range(N):
        print(board[x])

    start_x, start_y, size = find_square()
    print("정사각형", start_x, start_y, size)
    if size == 0:
        break
    rotate(start_x, start_y, size)

    for x in range(N):
        for y in range(N):
            if board[x][y] == 10:
                outdoor = [x, y]

    for x in range(N):
        print(board[x])
    print(move_count)
    print()

print(move_count)
print(outdoor[0]+1, outdoor[1]+1)

