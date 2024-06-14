from heapq import heappop, heappush

n, m, k = map(int, input().split())

people = []
people_info = [[] for _ in range(m)]
board = []
mono_board = [[0 for _ in range(n)] for _ in range(n)]
mono_num_board = [[-1 for _ in range(n)] for _ in range(n)]
mono_list = [[]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            board[i][j] -= 1
            heappush(people, [board[i][j], i, j])
            mono_board[i][j] = k
            mono_num_board[i][j] = board[i][j]
            mono_list[0].append([board[i][j], i, j])
        else:
            board[i][j] = -1


people_direction = list(map(int, input().split()))
for i in range(m):
    people_direction[i] -= 1

for i in range(m):
    for j in range(4):
        aa, bb, cc, dd = map(int, input().split())
        people_info[i].append([aa-1, bb-1, cc-1, dd-1])




answer = 0
while True:
    answer += 1
    new_people = []
    new_board = [[-1 for _ in range(n)] for _ in range(n)]
    mono_list.append([])
    while people:
        people_count = len(people)
        num, x, y = heappop(people)
        d = people_direction[num]
        direction_order = people_info[num][d]

        isMove = 0
        for i in range(4):
            md = direction_order[i]
            mx = x + dx[md]
            my = y + dy[md]
            if mx < 0 or mx >= n or my < 0 or my >= n or mono_board[mx][my] != 0:
                continue
            if new_board[mx][my] != -1:
                isMove = 1
                break
            isMove = 1
            new_board[mx][my] = num
            heappush(new_people, [num, mx, my])
            mono_list[-1].append([num, mx, my])
            people_direction[num] = md
            break
        if isMove == 0:
            for i in range(4):
                md = direction_order[i]
                mx = x + dx[md]
                my = y + dy[md]
                if 0 <= mx < n and 0 <= my < n and mono_num_board[mx][my] == num:
                    if new_board[mx][my] != -1:
                        break
                    new_board[mx][my] = num
                    heappush(new_people, [num, mx, my])
                    mono_list[-1].append([num, mx, my])
                    people_direction[num] = md
                    break

    if len(new_people) == 1 or answer >= 1000:
        break

    visit = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(mono_list)-1):
        for num, x, y in mono_list[i]:
            if visit[x][y] == 0:
                mono_board[x][y] -= 1
                visit[x][y] = 1
                if mono_board[x][y] <= 0:
                    mono_board[x][y] = 0
                    mono_num_board[x][y] = -1
    for num, x, y in mono_list[-1]:
        mono_board[x][y] = k
        mono_num_board[x][y] = num

    people = new_people
    board = new_board

if answer == 1000:
    print(-1)
else:
    print(answer)
