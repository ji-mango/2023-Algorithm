'''
'숫자고르기'
'''
# 24.01.30 15:12 ~ 17:35
import sys
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

visit = [0 for _ in range(N)]
answer = set()
def dfs(index):
    visit[index] = 1
    if check[index] == 2:
        return
    else:
        check[index] += 1
        if check[index] == 2:
            answer.add(index)
        dfs(array[index]-1)

for i in range(N):
    value = array[i] - 1
    if visit[value] == 0:
        check = [0 for _ in range(N)]
        dfs(i)
    visit[i] = 1

print(len(answer))
answer = list(answer)
answer.sort()
for i in range(len(answer)):
    print(answer[i] + 1)
