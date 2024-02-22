'''
'여행 가자'
'''
# 24.02.22 14:18 ~ 14:43
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

parent = list(range(N+1))
for i in range(N):
    array = list(map(int, input().split()))
    for j in range(N):
        if array[j] == 1:
            a, b = i + 1, j + 1
            if find_parent(a) != find_parent(b):
                union(a, b)

goal = list(map(int, input().split()))
answer = "YES"
node = find_parent(goal[0])

for i in range(1, M):
    if node != find_parent(goal[i]):
        answer = "NO"
        break

print(answer)

