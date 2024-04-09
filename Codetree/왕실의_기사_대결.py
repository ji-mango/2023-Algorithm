# 24.03.27 15:30~ 19:30

import sys
input = sys.stdin.readline
from collections import deque

def find_push(number, d):
    push_list = [number]
    queue = deque()
    queue.append([person_list[number][0], person_list[number][1]])
    visit = [[0 for _ in range(L)] for _ in range(L)]
    visit[person_list[number][0]][person_list[number][1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in [-1, 1]:
            md = (d + i) % 4
            mx = x + dx[md]
            my = y + dy[md]

            if 0 <= mx < L and 0 <= my < L and person_board[mx][my] == person_board[x][y]:
                if visit[mx][my] == 0:
                    visit[mx][my] = 1
                    queue.append([mx, my])

        mx = x + dx[d]
        my = y + dy[d]
        if mx < 0 or mx >= L or my < 0 or my >= L or board[mx][my] == 2:
            return []
        elif person_board[mx][my] != -1:
            if person_board[mx][my] not in push_list:
                push_list.append(person_board[mx][my])
            visit[mx][my] = 1
            queue.append([mx, my])

    return push_list


def move(number, d):
    r, c, h, w, k = person_list[number]
    if d == 0 or d == 2:
        if d == 0:
            insert_r = r - 1
            delete_r = h + r - 1
        if d == 2:
            insert_r = h + r
            delete_r = r
        copy_c = c
        for _ in range(w):
            person_board[delete_r][copy_c] = -1
            person_board[insert_r][copy_c] = number

            copy_c = copy_c + dy[1]

    if d == 1 or d == 3:
        if d == 1:
            insert_c = c+w
            delete_c = c
        if d == 3:
            insert_c = c - 1
            delete_c = c+w - 1
        copy_r = r
        for _ in range(h):
            person_board[copy_r][delete_c] = -1
            person_board[copy_r][insert_c] = number

            copy_r = copy_r + dx[2]

    person_list[number][0] = r + dx[d]
    person_list[number][1] = c + dy[d]


def damage(number):
    x, y, h, w, k = person_list[number]
    for i in range(x, x+h):
        for j in range(y, y+w):
            if board[i][j] == 1:
                person_list[number][4] -= 1

    if person_list[number][4] <= 0:
        person_list[number][4] = 0

        for i in range(x, x + h):
            for j in range(y, y + w):
                person_board[i][j] = -1




L, N, Q = map(int, input().split())  # 체스판 크기, 기사 수, 명령 수
board = []
person_board = [[-1 for _ in range(L)] for _ in range(L)]
person_list = []
origin_k = []
for i in range(L):
    board.append(list(map(int, input().split())))

for index in range(N):
    r, c, h, w, k = map(int, input().split())
    for i in range(r-1, r-1+h):
        for j in range(c-1, c-1+w):
            person_board[i][j] = index

    person_list.append([r-1, c-1, h, w, k])
    origin_k.append(k)

dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]
for i in range(L):
    print(person_board[i])
print()

for _ in range(Q):
    i, d = map(int, input().split())
    i = i-1
    print(i, d)
    if person_list[i][4] == 0:
        continue

    push_list = find_push(i, d)
    print(push_list)
    if push_list != []:
        for temp in range(len(push_list)-1, 0, -1):
            number = push_list[temp]
            move(number, d)
            damage(number)
        move(push_list[0], d)
    for i in range(L):
        print(person_board[i])
    print(person_list)
    print()

answer = 0
for i in range(len(origin_k)):
    if person_list[i][4] != 0:
        answer += origin_k[i] - person_list[i][4]

print(answer)
