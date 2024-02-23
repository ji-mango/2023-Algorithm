'''
'줄세우기'
'''
# 24.02.23 15:22 ~ 16:51(다)

N = int(input())
children = []
for i in range(N):
    children.append(int(input()))

d = [1] * N
for i in range(1, N):
    temp = 0
    for j in range(i-1, -1, -1):
        if children[i] > children[j]:
            temp = max(temp, d[j])
    d[i] = temp + 1

print(N - max(d))

