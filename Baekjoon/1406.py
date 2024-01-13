'''
'에디터'
'''
# 24.01.13
import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
M = int(input())
for i in range(M):
    command = list(input().split())

    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])

left.extend(reversed(right))        #  iterable의 각 항목을 넣기 위해 append대신 extend 사용
print(''.join(left))
