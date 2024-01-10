'''
'쿠키의 신체 측정'
'''
# 24.01.10
N = int(input())
array = []
for i in range(N):
        array.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

heart = [-1, -1]
for i in range(N):
    for j in range(N):
        if array[i][j] == '*':
            heart = [i+1, j]
            break
    if heart != [-1, -1]:
        break

# 왼팔 길이 구하기
left_arm = 0
present = [heart[0], heart[1]]
while True:
    mx = present[0] + dx[2]
    my = present[1] + dy[2]

    if my < 0:
        break
    elif array[mx][my] != '*':
        break
    else:
        present = [mx, my]
        left_arm += 1

# 오른팔 길이 구하기
right_arm = 0
present = [heart[0], heart[1]]
while True:
    mx = present[0] + dx[3]
    my = present[1] + dy[3]

    if my >= N:
        break
    elif array[mx][my] != '*':
        break
    else:
        present = [mx, my]
        right_arm += 1

# 허리 길이 구하기
waist = 0
present = [heart[0], heart[1]]
while True:
    mx = present[0] + dx[1]
    my = present[1] + dy[1]

    if array[mx][my] != '*':
        break
    else:
        present = [mx, my]
        waist += 1

# 왼다리 길이 구하기
left_leg = 1
present = [heart[0] + waist + 1, heart[1] - 1]
while True:
    mx = present[0] + dx[1]
    my = present[1] + dy[1]

    if mx >= N:
        break
    elif array[mx][my] != '*':
        break
    else:
        present = [mx, my]
        left_leg += 1

# 오른다리 길이 구하기
right_leg = 1
present = [heart[0] + waist + 1, heart[1] + 1]
while True:
    mx = present[0] + dx[1]
    my = present[1] + dy[1]

    if mx >= N:
        break
    elif array[mx][my] != '*':
        break
    else:
        present = [mx, my]
        right_leg += 1


print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
