'''
'주사위 굴리기'
'''

# 24.04.02 21:34 ~ 12:03
def change_center(index):
    present = dice[move_center[index][0][0]]
    for i in range(4):
        a, b = move_center[index][i]
        present, dice[b] = dice[b], present

N, M, x, y, K = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 주사위 모양
#   0
# 4 2 5
#   1
#   3

move_center = [[[5, 2], [2, 4], [4, 3], [3, 5]], [[4, 2], [2, 5], [5, 3], [3, 4]],
               [[0, 2], [2, 1], [1, 3], [3, 0]], [[1, 2], [2, 0], [0, 3], [3, 1]]]

move = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]
for i in range(K):
    d = move[i] - 1
    mx = x + dx[d]
    my = y + dy[d]
    if mx < 0 or mx >= N or my < 0 or my >= M:
        continue

    x, y = mx, my
    change_center(d)
    if board[x][y] == 0:
        board[x][y] = dice[2]
    else:
        dice[2] = board[x][y]
        board[x][y] = 0
    print(dice[3])
