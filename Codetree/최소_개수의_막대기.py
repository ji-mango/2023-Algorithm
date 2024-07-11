INF = int(1e9)

n, m = map(int, input().split())

shadow = []
for i in range(n):
    shadow.append(list(input()))

answer = INF

def find_shadow():
    for i in range(n):
        for j in range(m):
            if shadow[i][j] == '*':
                return [i, j]
    return -1


def dfs(count):
    global answer

    start = find_shadow()
    if start == -1:
        answer = min(count, answer)
        return

    # 가로로 막대기 놓을 때
    coordinate = [start]
    x, y = start
    shadow[x][y] = '.'
    while True:
        y += 1
        if y >= m or shadow[x][y] == '.':
            break
        coordinate.append([x, y])
        shadow[x][y] = '.'
    dfs(count + 1)
    for a, b in coordinate:
        shadow[a][b] = '*'

    # 세로로 막대기 놓을 때
    coordinate = [start]
    x, y = start
    shadow[x][y] = '.'
    while True:
        x += 1
        if x >= n or shadow[x][y] == '.':
            break
        coordinate.append([x, y])
        shadow[x][y] = '.'
    dfs(count + 1)
    for a, b in coordinate:
        shadow[a][b] = '*'

dfs(0)
print(answer)
