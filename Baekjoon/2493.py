'''
'탑'
'''
# 24.01.22
import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))

answer = [0 for _ in range(N)]
stack = []
for i in range(N):
    present = tower[i]
    while stack and present > tower[stack[-1]]:
        stack.pop()

    if stack and tower[stack[-1]] > present:
        answer[i] = stack[-1] + 1

    stack.append(i)

print(*answer)
