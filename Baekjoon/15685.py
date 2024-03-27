'''
'드래곤 커브'
'''

# 24.03.27
N = int(input())

dx = [0, -1, 0, 1]  # 우, 상, 좌, 하
dy = [1, 0, -1, 0]

game = []
X = 0
Y = 0
for i in range(N):
    y, x, d, g = map(int, input().split())
    game.append([x, y, d, g])

board = [[0 for _ in range(101)] for _ in range(101)]

for x, y, d, g in game:
    array = [[x, y]]
    board[x][y] = 1

    x += dx[d]
    y += dy[d]
    array.append([x, y])
    board[x][y] = 1
    generation = 1

    while generation <= g:
        generation += 1
        length = len(array)
        new_array = [i for i in array]

        for i in range(length-1, 0, -1):
            if array[i][0] < array[i-1][0]:
                d = 2
            elif array[i][0] > array[i-1][0]:
                d = 0
            elif array[i][1] < array[i-1][1]:
                d = 3
            else:
                d = 1

            mx = new_array[-1][0] + dx[d]
            my = new_array[-1][1] + dy[d]
            new_array.append([mx, my])
            board[mx][my] = 1

        array = new_array

answer = 0
for i in range(1, 101):
    for j in range(1, 101):
        if board[i-1][j-1] == 1 and board[i-1][j] == 1 and board[i][j-1] == 1 and board[i][j] == 1:
            answer += 1

print(answer)
