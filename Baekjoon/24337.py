'''
'가희와 탑'
'''

# 24.03.19 15:50 ~ 16:52
N, a, b = map(int, input().split())

if a >= b:
    tower = list(range(1, a + 1))
    tower += list(range(b-1, 0, -1))
else:
    tower = list(range(1, a))
    tower += list(range(b, 0, -1))

if len(tower) > N:      # 최소로 필요한 원소의 개수보다 N이 더 작을 경우는 불가능하므로 -1 출력
    print(-1)
else:
    if a == 1:
        tower = [tower.pop(0)] + [1] * (N-len(tower)-1) + tower
    else:
        tower = [1] * (N-len(tower)) + tower
    print(*tower)


