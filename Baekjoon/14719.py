'''
'빗물'
'''
# 24.01.22 17:18 ~ 17:37
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))

board = [[0 for _ in range(W)] for _ in range(H)]
for i in range(W):
    for j in range(block[i]):
        board[j][i] = 1

answer = 0
for i in range(H):
    start = -1
    end = -1
    count = 0
    for j in range(W):
        if board[i][j] == 1:
            if start == -1:
                start = j
            else:
                end = j
                count += (end - start - 1)
                start = j
    answer += count

print(answer)

