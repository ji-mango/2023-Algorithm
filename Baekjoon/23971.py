'''
ZOAC 4
'''
# 24.01.10
H, W, N, M = map(int, input().split())

answer = 0
column = W // (M+1)
row = H // (N+1)
if W % (M+1) != 0:
    column += 1
if H % (N+1) != 0:
    row += 1

answer = row * column
print(answer)