'''
'집합'
'''
# 24.01.10
import sys
input = sys.stdin.readline

M = int(input())
array = [0 for _ in range(21)]

for i in range(M):
    enter = list(input().split())
    if len(enter) == 2:
        b = int(enter[1])
    a = enter[0]

    if a == 'add':
        array[b] = 1
        continue
    elif a == 'remove':
        array[b] = 0
        continue
    elif a == 'check':
        print(array[b])
        continue
    elif a == 'toggle':
        array[b] = 0 if array[b] else 1
        continue
    elif a == 'all':
        array = [1 for _ in range(21)]
        continue
    elif a == 'empty':
        array = [0 for _ in range(21)]
        continue
