# 다시

N, Q, T = map(int, input().split())

plants = [0 for _ in range(100002)]
for i in range(Q):
    L, R = map(int, input().split())
    plants[L] += 1
    plants[R+1] -= 1

flag = 0
for i in range(1, N+1):
    plants[i] += plants[i-1]

    if plants[i] == T:
        flag = 1
        print(i, end=' ')

if flag == 0:
    print(-1)

