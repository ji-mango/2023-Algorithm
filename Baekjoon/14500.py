'''
'테트로미노
'''

# 24.04.03 14:00 ~ 16:20
import sys
input = sys.stdin.readline

def dfs(x, y, sumValue, depth):
    global answer
    if depth == 4:
        answer = max(answer, sumValue)
        return

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= N or my < 0 or my >= M or visit[mx][my] == 1:
            continue
        visit[mx][my] = 1
        dfs(mx, my, sumValue + board[mx][my], depth + 1)
        visit[mx][my] = 0

def find_different(a, b):
    maxValue = 0
    for i in range(4):
        x, y = a, b
        sumValue = board[x][y]
        for j in range(2):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= N or my < 0 or my >= M:
                break
            x, y = mx, my
            sumValue += board[x][y]
            if j == 0:
                temp = 0
                for index in [1, 3]:
                    mx = x + dx[(i+index) % 4]
                    my = y + dy[(i+index) % 4]
                    if 0 <= mx < N and 0 <= my < M:
                        temp = max(temp, board[mx][my])

                sumValue += temp


        maxValue = max(maxValue, sumValue)
    return maxValue

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 상, 좌, 하, 우
dy = [0, -1, 0, 1]


answer = 0
visit = [[0 for _ in range(M)] for _ in range(N)]
for x in range(N):
    for y in range(M):
        visit[x][y] = 1
        dfs(x, y, board[x][y], 1)
        visit[x][y] = 0
        result = find_different(x, y)
        answer = max(answer, result)

print(answer)

