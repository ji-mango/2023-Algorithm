'''
'문자열 폭발'
'''
# 24.02.19 14:14 ~ 14:43
import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
len_bomb = len(bomb)

stack = []
for i in string:
    stack.append(i)
    if i == bomb[-1] and len(stack) >= len_bomb:
        index = -1
        while abs(index) <= len_bomb:
            if stack[index] == bomb[index]:
                index -= 1
            else:
                break

        if abs(index) == len_bomb + 1:
            for _ in range(len_bomb):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")

