'''
'공유기 설치'
'''
# 24.02.15 14:48 ~ 16:24(다)
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

router = []
for i in range(N):
    router.append(int(input()))

router.sort()

start = 1                       # 최소 거리
end = router[-1] - router[0]    # 최대 거리

answer = 0
while start <= end:
    standard = router[0]
    count = 1
    mid = (start + end) // 2

    for i in range(1, N):
        if router[i] - standard >= mid:
            count += 1
            standard = router[i]

    if count >= C:         # mid 길이만큼 설치한 공유기 개수가 C보다 많으면 공유기간 거리를 넓힘
        answer = mid
        start = mid + 1
    else:
        end = mid - 1       # mid 길이만큼 설치한 공유기 개수가 C보다 적으면 공유기간 거리를 좁힘

print(answer)
