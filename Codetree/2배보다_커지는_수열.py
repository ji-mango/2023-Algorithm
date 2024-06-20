n, m = map(int, input().split())

d = [[] for _ in range(n+1)]
d[1] = [1 for i in list(range(m))]  # [맨앞이 1인 수열의 개수, 맨앞이 2인 수열의 개수, ...]

for i in range(2, n+1):
    for j in range(1, len(d[i-1]), 2):
        d[i].append(sum(d[i-1][j:]) % 1000000007)

print(d)
print(sum(d[-1]) % 1000000007)
