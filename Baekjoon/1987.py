'''
'알파벳'
'''
#24.02.13 16:41 ~ 17:47
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
def dfs(x, y, depth):
    global answer
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= R or my < 0 or my >= C or alphabet[ord(board[mx][my]) - 65] == True:
            continue
        alphabet[ord(board[mx][my]) - 65] = True
        dfs(mx, my, depth+1)
        alphabet[ord(board[mx][my]) - 65] = False

    answer = max(depth, answer)

alphabet = [False] * 26
alphabet[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)

print(answer)
