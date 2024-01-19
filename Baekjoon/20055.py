'''
'컨베이어 벨트 위의 로봇'
'''
# 24.01.19
from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))

def rotation(belt, robot):
    new_belt = [0]
    for i in range(2 * N - 1):
        new_belt.append(belt[i])
    new_belt[0] = belt[-1]

    for i in range(len(robot)):
        robot[i] = robot[i] + 1
    if robot and robot[0] == N-1:
        robot.popleft()

    return new_belt, robot

step = 1
robot = deque()

while True:
    # step1
    belt, robot = rotation(belt, robot)

    # step2
    for i in range(len(robot)):
        if (i == 0 or (robot[i-1] != robot[i] + 1)) and belt[robot[i]+1] > 0:
            robot[i] = robot[i]+1
            belt[robot[i]] -= 1
    if robot and robot[0] == N-1:
        robot.popleft()

    # step3
    if belt[0] != 0:
        robot.append(0)
        belt[0] -= 1
        if robot and robot[0] == N - 1:
            robot.popleft()

    # step4
    cnt = 0
    for i in range(2 * N):
        if belt[i] == 0:
            cnt += 1

    if cnt >= K:
        print(step)
        break
    step += 1
