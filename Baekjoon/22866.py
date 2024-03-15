'''
'탑 보기'
'''

# 24.03.15 17:10 ~ 19:00 다
import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))

stack = []
answer = [[0, -1] for _ in range(N)]
for i in range(N):
    height = tower[i]
    while stack:
        if stack[-1][1] <= height:
            stack.pop()
        else:
            break

    if stack:
        answer[i][0] += len(stack)
        answer[i][1] = stack[-1][0]
    stack.append([i, height])

stack = []
for i in range(N-1, -1, -1):
    height = tower[i]
    while stack:
        if stack[-1][1] <= height:
            stack.pop()
        else:
            break

    if stack:
        answer[i][0] += len(stack)
        if answer[i][1] == -1:
            answer[i][1] = stack[-1][0]
        else:
            if abs(answer[i][1] - i) > abs(stack[-1][0] - i):
                answer[i][1] = stack[-1][0]
            elif abs(answer[i][1] - i) == abs(stack[-1][0] - i):
                answer[i][1] = min(answer[i][1], stack[-1][0])
    stack.append([i, height])

for i in range(N):
    if answer[i][0] == 0:
        print(0)
    else:
        print(answer[i][0], answer[i][1]+1)
