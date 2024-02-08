'''
'좋다'
'''
# 24.02.08 15:15 ~ 16:16
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

answer = 0
for i in range(0, N):
    left = 0
    right = N-1

    while left < right:
        if A[left] + A[right] == A[i]:
            answer += 1
            break
        elif A[left] + A[right] < A[i]:
            if left+1 == i:
                left += 2
            else:
                left += 1
        else:
            if right-1 == i:
                right -= 2
            else:
                right -= 1

left = 0
right = N-2
while left < right:                     # 위 for문에서 매번 if분기문을 돌지 않기 위해 맨 처음과 맨 끝은 따로 빼주기
    if A[left] + A[right] == A[N-1]:
        answer += 1
        break
    elif A[left] + A[right] < A[N-1]:
        left += 1
    else:
        right -= 1

left = 1
right = N-1
while left < right:
    if A[left] + A[right] == A[0]:
        answer += 1
        break
    elif A[left] + A[right] < A[0]:
        left += 1
    else:
        right -= 1

print(answer)
