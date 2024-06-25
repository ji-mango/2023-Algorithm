'''
'뉴스 전하기'
'''

# 24.06.25
N = int(input())

input_list = list(map(int, input().split()))

tree = [[] for _ in range(N)]
for i in range(1, N):
    master = input_list[i]
    tree[master].append(i)

time = [0] * N

def dp(m):
    child_t = []
    for child in tree[m]:
        dp(child)
        child_t.append(time[child])
    if tree[m] == []:
        child_t.append(0)

    child_t.sort(reverse=True)

    need_t = [child_t[i]+i+1 for i in range(len(child_t))]
    time[m] = max(need_t)

dp(0)
print(time[0]-1)

