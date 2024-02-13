'''
'부분합'
'''
# 24.02.13 15:31 ~ 16:29
import sys
input = sys.stdin.readline
INF = int(1e9)

N, S = map(int, input().split())
array = list(map(int, input().split()))

add_array = [0]
for i in range(N):                              # 누적합 구하기
    add_array.append(add_array[i]+array[i])

answer = INF
for i in range(N, -1, -1):                      # 각 요소가 끝 수 일 때의 최소길이 이진탐색으로 구하기
    start = max(0, i-answer)
    end = i-1
    check = INF

    while start <= end:
        mid = (start + end) // 2
        if add_array[i] - add_array[mid] > S:
            check = i-mid
            start = mid + 1
        elif add_array[i] - add_array[mid] < S:
            end = mid - 1
        else:
            check = i-mid
            break

    answer = min(check, answer)
    if answer == 1:
        break

if answer == INF:
    print(0)
else:
    print(answer)
