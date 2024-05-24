'''
'컵라면'
'''
# 다시

from heapq import heappop, heappush

N = int(input())
problem = []
for i in range(N):
    problem.append(list(map(int, input().split())))

problem.sort()

queue = []
for i in problem:
    heappush(queue, i[1])
    if len(queue) > i[0]:
        heappop(queue)

print(sum(queue))
