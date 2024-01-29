'''
'전구와 스위치'
'''
# 24.01.29 14:45 ~ 15:53(다)
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
light = list(input().strip())
goal = list(input().strip())

def switch(arr, index):
    if index-1 >= 0:
        arr[index-1] = '0' if arr[index-1] == '1' else '1'
    arr[index] = '0' if arr[index] == '1' else '1'
    if index+1 < N:
        arr[index+1] = '0' if arr[index+1] == '1' else '1'

compare = [light[i] for i in range(N)]

answer1 = 0
for i in range(1, N):
    if light[i-1] != goal[i-1]:
        switch(light, i)
        answer1 += 1

if light[-1] != goal[-1]:
    answer1 = INF


switch(compare, 0)
answer2 = 1
for i in range(1, N):
    if compare[i-1] != goal[i-1]:
        switch(compare, i)
        answer2 += 1

if compare[-1] != goal[-1]:
    answer2 = INF


answer = min(answer1, answer2)
if answer == INF:
    print(-1)
else:
    print(answer)
