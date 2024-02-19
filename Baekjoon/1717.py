'''
'집합의 표현'
'''
# 24.02.19 15:06 ~ 15:26(공부용)
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i


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


for i in range(n+1):
    find_parent(i)

for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    else:
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")
